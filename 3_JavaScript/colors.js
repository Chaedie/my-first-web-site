var Links = {
  SetColor:function(color) {
    // var alist = document.querySelectorAll('a');
    // var i = 0;
    // while (i < alist.length) {
    //   alist[i].style.color = color;
    //   i = i + 1;
    // }
    $('a').css('color',color);
  },
}
var Body ={
  SetColor:function(color){
    // document.querySelector('body').style.color = color;
    $('body').css('color',color);
  },
  SetBackgroundColor:function(color){
    // document.querySelector('body').style.backgroundColor = color;
    $('body').css('backgroundColor',color);
  },
}
function FontChangeHandler(value) {
  var alist = document.querySelectorAll('a');
  var i = 0;
  if (value === 'night') {
    while (i < alist.length) {
      alist[i].style.color = 'powderblue';
      i = i + 1;
    }
  } else {
    while (i < alist.length) {
      alist[i].style.color = 'blue';
      i = i + 1;
    }
  }

}

function NightDayHandler(self) {
  if (self.value === 'night') {
    Body.SetBackgroundColor('black');
    Body.SetColor('white');
    self.value = 'day';
    //FontChangeHandler(self.value);
    Links.SetColor('powderblue');
  } else {
    Body.SetBackgroundColor('white');
    Body.SetColor('black');
    self.value = 'night'
    //FontChangeHandler(self.value);
    Links.SetColor('blue');
  }
}
