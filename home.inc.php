<?php

$pagetitle = 'Helios small hotel';
$jscript .= "
$(window).load(function() {
	$('.blueberry').blueberry(
		{
		interval : 3000 ,
		duration: 3000
		}
	);
});";
?>


<div class="blueberry">



  <ul class="slides">
    <li><img src="img/slider/00.jpg" /></li>
    <li><img src="img/slider/01.jpg" /></li>
    <li><img src="img/slider/1.jpg" /></li>
    <li><img src="img/slider/2.jpg" /></li>
    <li><img src="img/slider/3.jpg" /></li>
    <li><img src="img/slider/4.jpg" /></li>
    <li><img src="img/slider/5.jpg" /></li>
		<li><img src="img/fab/GARDEN/DSC_0121.jpg" /></li>
		<li><img src="img/fab/GARDEN/DSC_0054_edited.jpg" /></li>
		<li><img src="img/fab/GARDEN/DSC_0107_edited.jpg" /></li>

  </ul>
<!-- Optional, see options below -->
  <ul class="pager">
    <li><a href="#"><span></span></a></li>
    <li><a href="#"><span></span></a></li>
    <li><a href="#"><span></span></a></li>
    <li><a href="#"><span></span></a></li>
    <li><a href="#"><span></span></a></li>
    <li><a href="#"><span></span></a></li>
		<li><a href="#"><span></span></a></li>
		<li><a href="#"><span></span></a></li>
		<li><a href="#"><span></span></a></li>
		<li><a href="#"><span></span></a></li>

  </ul>
<!-- Optional, see options below -->
</div>

<div class="eightcol">
	<?php include 'texts/'.$lang.'/home-news.html'; ?>
	<p>To read our safety measures against COVID19 click here <a href=" https://drive.google.com/file/d/1B63DIQhLyCUuLVI6WBF3jFU9XRERPrZ5/view?fbclid=IwAR2Se56Gx0pL9ZEbm7pCIMUuhKM9iTuWXNVb4eKatPbDXaUNlmP6mIzneQw">Safety Measures</a></p>
	<div>
	<a href="booking"><img src="img/sticker.png"></a>
	</div>
</div>

<div class="fourcol last">
<!--	<div id="ahomead">
		<img src="img/logo-premium-coffee.png"/>
		php include 'texts/'.$lang.'/home-coffee.html'; ?>
	</div> -->
</div>
<div  class="fb-page" data-href="https://www.facebook.com/Hotel-Helios-Boukari-104786847869200/" data-tabs="timeline" data-width="" data-height="" data-small-header="true" data-adapt-container-width="true" data-hide-cover="false" data-show-facepile="true"></div>
