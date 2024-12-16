function priority_swiper(){
    var priority = 0
    if(hexo.config.swiper.priority){
        priority = hexo.config.swiper.priority
    }
    else{
        priority = 0
    }
    return priority
}

hexo.extend.filter.register('after_generate',function() {
    var swiper = hexo.config.swiper.enable;
    if(swiper){
        var temple = hexo.config.swiper.temple_html.split("${temple_html_item}")
        var layout_name ='';
        var layout_type ='';
        var layout_index =0;
        layout_name = hexo.config.swiper.layout.name;
        layout_type = hexo.config.swiper.layout.type;
        layout_index =  hexo.config.swiper.layout.index;
        var get_layout = ''
        if (layout_type == 'class'){
            get_layout =  `document.getElementsByClassName('${layout_name}')[${layout_index}]`
        }else if (layout_type == 'id'){
            get_layout =  `document.getElementById('${layout_name}')`
        }else {
            get_layout =  `document.getElementById('${layout_name}')`
        }
        var temple_html_item = ''
        var posts_list = hexo.locals.get('posts').data;
        var new_posts_list =[]
        for (item of posts_list){
            if(item.swiper_index && item.swiper_desc){
                new_posts_list.push(item)
            }}
        function sortNumber(a,b)
        {
            return a.swiper_index - b.swiper_index
        }
        new_posts_list = new_posts_list.sort(sortNumber);
        new_posts_list = new_posts_list.reverse();
        for (item of new_posts_list){
            if(item.swiper_index && item.swiper_desc){
                temple_html_item += `<div class="blog-slider__item swiper-slide" style="width: 750px; opacity: 1; transform: translate3d(0px, 0px, 0px); transition-duration: 0ms"><div class="blog-slider__img"><img src="${item.swiper_cover||item.cover}" alt="${item.swiper_cover||item.cover}"/></div><div class="blog-slider__content"><span class="blog-slider__code">${item.date.format('YYYY-MM-DD')}</span><a class="blog-slider__title" href="${item.path}">${item.title}</a><div class="blog-slider__text">${item.swiper_desc}</div><a class="blog-slider__button" href="${item.path}">详情</a></div></div>`;
            }
        }
        var temple_html =`${temple[0]}<div class="blog-slider__wrp swiper-wrapper" style="transition-duration: 0ms">${temple_html_item}</div><div class="blog-slider__pagination swiper-pagination-clickable swiper-pagination-bullets"></div>${temple[1]}`;
        var script_text = ` <script data-pjax>if(${get_layout} && location.pathname =='${hexo.config.swiper.enable_page}'){
    
    var parent = ${get_layout};
    var child = '${temple_html}';
    console.log('已挂载swiper')
    parent.insertAdjacentHTML("afterbegin",child)}
     </script>
<script data-pjax src="https://cdn.jsdelivr.net/gh/Zfour/Butterfly-swiper/swiper/swiper.min.js"></script>
<script data-pjax src="https://cdn.jsdelivr.net/gh/Zfour/Butterfly-swiper@0.18/swiper/swiperindex.js"></script>
<style>${hexo.config.swiper.plus_style}</style>`;
        hexo.extend.injector.register('head_end',`<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/Zfour/Butterfly-swiper/swiper/swiper.min.css"><link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/Zfour/Butterfly-swiper/swiper/swiperstyle.css">`, "default");
        hexo.extend.injector.register('body_end',script_text, "default");
    }

},priority_swiper())