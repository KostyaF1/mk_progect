/**
 * Based on: jqFancyTransitions - jQuery plugin
 * @version: 1.8 (2010/06/13)
 * @requires jQuery v1.2.2 or later 
 * @author Ivan Lazarevic
 * Examples and documentation at: http://www.workshop.rs/projects/jqfancytransitions
 
 * Dual licensed under the MIT and GPL licenses:
 *   http://www.opensource.org/licenses/mit-license.php
 *   http://www.gnu.org/licenses/gpl.html
**/
(function($) {
	var opts = new Array;
	var img = new Array;
	var order = new Array;
	var imgInc = new Array;
	var inc = new Array;
	var stripInt = new Array;
	var defInt = new Array;
	
	$.fn.jqFancyTransitions = function(options){
	
	init = function(el){

		opts[el.id] = $.extend({}, $.fn.jqFancyTransitions.defaults, options);
		opts[el.id].animated = 0;
		img[el.id] = new Array(); // images array
		order[el.id] = new Array(); // strips order array
		imgInc[el.id] = 0;
		inc[el.id] = 0;
		defInt[el.id] = 0;
		
		params = opts[el.id];

		if(params.effect == 'zipper'){params.direction = 'alternate';params.position = 'alternate';}
		if(params.effect == 'wave'){params.direction = 'alternate';params.position = 'top';}
		if(params.effect == 'curtain'){params.direction = 'alternate';params.position = 'curtain';}	

		// width of strips
		stripWidth = parseInt(params.width / params.strips); 
		gap = params.width - stripWidth*params.strips; // number of pixels
		stripLeft = 0;

		// create images arrays
		$.each($('#'+el.id+' img'), function(i,item){
			img[el.id][i] = $(item).attr('src');
			$(item).hide();
		});

		// set panel
		$('#'+el.id).css({
			'background-image':'url('+img[el.id][0]+')',
			'width': params.width,
			'height': params.height,
			'position': 'relative',
			'background-position': 'top left'
		});

		odd = 1;
		// creating bars
		// and set their position
		for(j=1; j < params.strips+1; j++){
			
			if( gap > 0){
				tstripWidth = stripWidth + 1;
				gap--;
			} else {
				tstripWidth = stripWidth;
			}

			$('#'+el.id).append("<div class='ft-"+el.id+"' id='ft-"+el.id+j+"' style='width:"+tstripWidth+"px; height:"+params.height+"px; float: left; position: absolute;'></div>");
							
			// positioning bars
			$("#ft-"+el.id+j).css({ 
				'background-position': -stripLeft +'px top',
				'left' : stripLeft 
			});
			
			stripLeft += tstripWidth;

			if(params.position == 'bottom'){
				$("#ft-"+el.id+j).css( 'bottom', 0 );
			}
			if (j%2 == 0 && params.position == 'alternate'){
				$("#ft-"+el.id+j).css( 'bottom', 0 );
			}
			
			// bars order
			if(params.direction == 'fountain' || params.direction == 'fountainAlternate'){
				// fountain
				order[el.id][j-1] = parseInt(params.strips/2) - (parseInt(j/2)*odd);
				order[el.id][params.strips-1] = params.strips; // fix for odd number of bars
				odd *= -1;
			} else {
				// linear
				order[el.id][j-1] = j;
			}
		}
	};

	// without cycle and delay
	$.startAnimation = function(el){

		opts[el.id].last = 'start';

		if(opts[el.id].start == true || opts[el.id].stop == true){
			return;
		}
		opts[el.id].start = true;
		clearTimeout(defInt[el.id]);

		$.transition(el);
	};

	// without cycle and delay
	$.stopAnimation = function(el){

		opts[el.id].last = 'stop';

		if(opts[el.id].stop == true || opts[el.id].start == true){
			return;
		}
		
		opts[el.id].stop = true;
		clearTimeout(defInt[el.id]);
		
		opts[el.id].oldStripDelay = opts[el.id].stripDelay;
		opts[el.id].oldStripSpeed = opts[el.id].stripSpeed;
		opts[el.id].stripDelay = 0;
		opts[el.id].stripSpeed = 0;

		$.transition(el);
	}

	$.callStrip = function(id){
		$.strips(order[id][inc[id]], id);
	}

	// transition
	$.transition = function(el, direction){

		stripInt[el.id] = window.setTimeout('$.callStrip("'+el.id+'")', opts[el.id].stripDelay);
		
		$('#'+el.id).css({'background-image': 'url('+img[el.id][imgInc[el.id]]+')'});
		
		if(typeof(direction) == "undefined")
			imgInc[el.id]++;
		else
			if(direction == 'prev')
				imgInc[el.id]--;
			else
				imgInc[el.id] = direction;

		if  (imgInc[el.id] == img[el.id].length) {
			imgInc[el.id] = 0;
		}
		
		if (imgInc[el.id] == -1){
			imgInc[el.id] = img[el.id].length-1;
		}
		
		inc[el.id] = 0;

		if(opts[el.id].direction == 'random')
			$.fisherYates (order[el.id]);
			
		if((opts[el.id].direction == 'right' && order[el.id][0] == 1) 
			|| opts[el.id].direction == 'alternate'
			|| opts[el.id].direction == 'fountainAlternate')			
				order[el.id].reverse();
			
	};

	// callback on animation
	$.onAnimateFinish = function(id){

		opts[id].animated++;

		if(opts[id].animated  == opts[id].strips){
			if(opts[id].start){
				opts[id].start = false;
				if(opts[id].last=='stop'){
					clearTimeout(defInt[id]);
					defInt[id] = setTimeout('$("#'+id+'").mouseleave();', 0);
				}
			}
			else{
				opts[id].stop = false;	
				if(opts[id].last=='start'){
					clearTimeout(defInt[id]);
					defInt[id] = setTimeout('$("#'+id+'").mouseenter();', 0);
				}
				opts[id].stripDelay = opts[id].oldStripDelay;
				opts[id].stripSpeed = opts[id].oldStripSpeed;
			}
			
			opts[id].animated = 0;
		}
	}

	// strips animations
	$.strips = function(itemId, id){

		if (inc[id] == opts[id].strips) {
			clearInterval(stripInt[id]);
			return;
		}
		if(opts[id].position == 'curtain'){
			currWidth = $('#ft-'+id+itemId).width();
			$('#ft-'+id+itemId).css({width: 0, opacity: 0, 'background-image': 'url('+img[id][imgInc[id]]+')'}).animate({width: currWidth, opacity: 1}, opts[id].stripSpeed, 'linear', function(){
				$.onAnimateFinish(id);
			});
		}
		else if(opts[id].position == 'fade'){
			currWidth = $('#ft-'+id+itemId).width();
			$('#ft-'+id+itemId).css({ opacity: 0, 'background-image': 'url('+img[id][imgInc[id]]+')' }).animate({ opacity: 1 }, opts[id].stripSpeed, 'linear', function(){
				$.onAnimateFinish(id);
			});
		}
		else {
			$('#ft-'+id+itemId).css({height: 0, opacity: 0, 'background-image': 'url('+img[id][imgInc[id]]+')'}).animate({height: opts[id].height, opacity: 1}, opts[id].stripSpeed, 'linear', function(){
				$.onAnimateFinish(id);
			});
		}
		
		inc[id]++;
		stripInt[id] = window.setTimeout('$.callStrip("'+id+'")', opts[id].stripDelay);
	};

	// shuffle array function
	$.fisherYates = function(arr) {
	  var i = arr.length;
	  if ( i == 0 ) return false;
	  while ( --i ) {
	     var j = Math.floor( Math.random() * ( i + 1 ) );
	     var tempi = arr[i];
	     var tempj = arr[j];
	     arr[i] = tempj;
	     arr[j] = tempi;
	   }
	}	
		
	this.each (
		function(){init(this);}
	);
		
	};

	// default values
	$.fn.jqFancyTransitions.defaults = {	
		width: 500, // width of panel
		height: 300, // height of panel
		strips: 10, // number of strips
		delay: 5000, // delay between images in ms
		stripDelay: 50, // delay beetwen strips in ms
		stripSpeed: 600,
		position: 'alternate', // top, bottom, alternate, curtain
		direction: 'fountainAlternate', // left, right, alternate, random, fountain, fountainAlternate
		effect: '' // curtain, zipper, wave
	};
	
})(jQuery);


$(document).ready(function(){

	$('.d_block').each(function(){
		$('#'+this.id).jqFancyTransitions({
			width: 229,
			height: 500,
			delay: 0,
			pause: true,
			effect: 'zipper', // wave, zipper, curtain
			position: 'top', // top, bottom, alternate, curtain
			direction: 'right',	// left, right, alternate, random, fountain, fountainAlternate
			stripDelay: 30,
			stripSpeed: 400,
			strips: 7
		});
	});

	$('.d_block').click(function(){
		location.href = $(this).find('a').attr('href');
	}).mouseenter(function(){
		$.startAnimation(this);
	}).mouseleave(function(){
		$.stopAnimation(this);
	});

	$('#d_auto_logos').roundCorner({
		top: ['#0A0A0A', '#ffffff'],
		bottom: ['#1E1E1E', '#ffffff'],
		sizex: 8,
		sizey: 8
	});

});