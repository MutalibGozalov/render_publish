
$(function() {
   var time_input = $("#add-form").children("div").eq(1).children("div").eq(1).children("input");
   time_input.attr("placeholder", "0h");


   var minute_input = $("#add-form").children("div").eq(1).children("div").eq(2).children();
   minute_input.attr("placeholder", "0m");

   var time_input = $("#edit-form").children("div").eq(1).children("div").eq(1).children("input");
   time_input.attr("placeholder", "0h");


   var minute_input = $("#edit-form").children("div").eq(1).children("div").eq(2).children();
   minute_input.attr("placeholder", "0m");

   var today = new Date();
   var dd = String(today.getDate()).padStart(2, '0');
   var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
   var yyyy = today.getFullYear();

   today = yyyy + '-' + mm + '-' + dd;
   this_month = yyyy + '-' + mm;

   $("input[name='today']").attr('value', today);
   $("input[name='month']").attr('value', this_month);

   $("input[name='today']").attr('max', today);
   $("input[name='month']").attr('max', this_month);

   inc_dec();
});

$(function() {
   $.ajax({
      type:'GET',
      url:'sidebar',
      success: function(response) {
         navs = $( '.sidebar .sidebar-nav li' );
         titles = $('.card-title');
         

         sc = "<b class='ms-5 px-1 text-warning'>"+ response['sc'] +"</b>"
         ac = "<b class='ms-2 px-1 text-warning'>"+ response['ac'] +"</b>"
         bc = "<b class='ms-5 px-1 text-warning'>"+ response['bc'] +"</b>"
         $(navs['1']).children().eq(0).append(sc);
         $(navs['2']).children().eq(0).append(ac);
         $(navs['3']).children().eq(0).append(bc);

         if (response['ac'] >99) {
            $(navs['2']).children().eq(0).children().eq(2).text("99+");
         }


         if ($('title').text().trim() == 'Services') {
            $(titles['0']).append(sc);
         } else if($('title').text().trim() == 'Transactions') {
            $(titles['0']).append(ac);
         } else if($('title').text().trim() == 'Barbers') {
            $(titles['0']).append(bc);
         }
      }
   });
});

function inc_dec() {
    //vars defined at <head> section
    var inc_d = Math.abs(ds-ds_b)/ds_b*100;
    var inc_m = Math.abs(ms-ms_b)/ms_b*100;

    $("#123456").text(Math.round(inc_d) + " %");
    $("#1234567").text(Math.round(inc_m) + " %");

    var danger = 'text-danger small pt-1 fw-bold';
    var success = 'text-success small pt-1 fw-bold';

    if (+ds < +ds_b) {
       $("#123456").attr('class', danger);
       $("#123456").parent().children().eq(2).text('| decrease | $'+ ds_b);
    }
    if (+ds > +ds_b) {
       $("#123456").attr('class', success);
       $("#123456").parent().children().eq(2).text('| increase | $'+ ds_b);
    }

    if (+ms < +ms_b) {
       $("#1234567").attr('class', danger);
       $("#1234567").parent().children().eq(2).text('| decrease | $'+ ms_b);
    }
    if (+ms > +ms_b) {
       $("#1234567").attr('class', success);
       $("#1234567").parent().children().eq(2).text('| increase | $'+ ms_b);
    }


    neut = 'text-muted small pt-1 fw-bold';
    if (+ds_b == 0) {
       $("#123456").attr('class', neut);
       $("#123456").text("");
       $("#123456").parent().children().eq(2).text('| yestarday: $ 0');
    }
    if (+ms_b == 0) {
       $("#1234567").attr('class', neut);
       $("#1234567").text("");
       $("#1234567").parent().children().eq(2).text('| last month: $ 0');
    }
}

const select = (el) => {
   el = el.trim()
   return document.querySelector(el)
}

$(document).on('click', '.toggle-sidebar-btn', function(e) {
   select('body').classList.toggle('toggle-sidebar');
});

$(document).on('click', '.list-edit', function(e){
   $("#edit-form").attr("sid", $(this).attr("sid"));
   $("input[name='name']").eq(0).val($(this).parent().parent().children().eq(0).text());
   $("input[name='prize']").eq(0).val($(this).parent().parent().children().eq(1).text().substring(1,));
   $("input[name='time']").eq(0).val($(this).parent().parent().children().eq(2).text().substring(0,1));
   $("#edit-form").children("div").eq(1).children("div").eq(2).children().val($(this).parent().parent().children().eq(2).text().substring(2,5));
});

$(document).on('click', '.list-delete', function(e){
   $("#delete-form").attr("sid", $(this).attr("sid"));
   $("input[name='name']").eq(2).val($(this).parent().parent().children().eq(0).text());
});

$(document).on('click', '.list-delete-barber', function(e){
   $("#delete-barber").attr("sid", $(this).attr("sid"));
   $("input[name='name']").eq(1).val($(this).parent().parent().children().eq(0).text());
});


$(document).on('submit', '#edit-form', function(e){
   e.preventDefault();
  
   var time_input = $(this).children("div").eq(1).children("div").eq(1).children("input");
   var hour = time_input.val();

   var minute_input = $(this).children("div").eq(1).children("div").eq(2).children();
   var minute = minute_input.val();

   if (minute == "") {
      minute = "0";
   }

   if (hour == "") {
      hour = "0";
   }
   

   time_input.val(hour);
   minute_input.val(minute);
  
   $.ajax({
      type:'POST',
      url:'services/'+ $(this).attr('sid') + '/',
      data: {
            Hour: $("input[name='time']").val(),
            Minute: $("input[name='time2']").val(),
            Name: $("input[name='name']").val(),
            Prize: $("input[name='prize']").val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
      },
      success: function(response) {
            location.reload();
      }
   });
});

$(document).on('submit', '#add-form', function(e){
   e.preventDefault();

   var time_input = $(this).children("div").eq(1).children("div").eq(1).children("input");
   var hour = time_input.val();

   var minute_input = $(this).children("div").eq(1).children("div").eq(2).children();
   var minute = minute_input.val();

   if (minute == "") {
      minute = "0";
   }

   if (hour == "") {
      hour = "0";
   }
   
   var post_time = (hour + ":" + minute + ":00");
   time_input.val(post_time);
   
   (this).submit();

});

$(document).on('submit', '#delete-form', function(e){
   e.preventDefault();

   $.ajax({
      type:'POST',
      url:'services/delete/'+ $(this).attr('sid') + '/',
      data: {
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
      },
      success: function(response) {
            location.reload();
      }
   });
});

$(document).on('submit', '#delete-barber', function(e){
   e.preventDefault();

   $.ajax({
      type:'POST',
      url:'barbers/delete/'+ $(this).attr('sid') + '/',
      data: {
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
      },
      success: function(response) {
            location.reload();
      }
   });
});


$(document).on('change', "input[name='today']", function(e) {
$.ajax({
      type:'POST',
      url:'summary',
      data: {
               
            //2022-11-06
            Month: $(this).val().substring(5,7),
            Day: $(this).val().substring(8,10),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
      },
      success: function(response) {
         $("#day_sum").text($("#day_sum").text()[0] + response.day_sum);
      }
   });

});

$(document).on('change', "input[name='month']", function(e) {
$.ajax({
      type:'POST',
      url:'summary',
      data: {
               
            //2022-11-06
            Month: $(this).val().substring(5,7),
            Day: '01',//$(this).val().substring(8,10),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
      },
      success: function(response) {
         $("#month_sum").text($("#month_sum").text()[0] + response.month_sum);
      }
   });

});

$(function() {
   navs = $( '.sidebar .sidebar-nav span' );
   nav_list = Object.values(navs);
   title = $( 'title' ).text().trim();
    $.each( navs, function( key, value ) { //keep 'key' parameter here cause function needs to know value is second and tho it doesnt represent not key parameter
    if ($(value).parent().text().trim() == title || $(value).parent().text().trim() == title.substring(0,9))
    {
        $(value).parent().removeClass( 'collapsed' );
    } 
    else if(!$(value).parent().hasClass('collapsed')) {
        $(value).parent().addClass('collapsed');
    }
    });
});

// --------------------------------------- FILTER TRANSACTIONS --------------------------------------//

var trlist = [];
$(function () {
    $.ajax({
    type:'get',
    url:'transactionsfilter',
    success: function(response){
        trlist = Object.values(response);
    }
    });
});
var from;
var to;


$(document).on('click', '#by_service', function(e) {
   from = $('input[name=from]').val(); //first index is 0;
   to = $('input[name=to]').val();
   if (!from || !to && from !== 0) {
      orderBy_list(0);
   } else {
      orderBy_list(0, from, to);
   }
});
$(document).on('click', '#by_tip', function(e) {
   from = $('input[name=from]').val();
   to = $('input[name=to]').val();
   if (!from || !to && from !== 0) {
      orderBy_list(3);
   } else {
      orderBy_list(3, from, to);
   }
});
$(document).on('click', '#by_outcome', function(e) {
   from = $('input[name=from]').val();
   to = $('input[name=to]').val();
   if (!from || !to && from !== 0) {
      orderBy_list(4);
   } else {
      orderBy_list(4, from, to);
   }
});

function orderBy_list(index, from=0, to=14) {
      trlist[0].sort(function(a, b){
         if (index == 0) {
            return (a[index] === b[index] ? 0 : (a[index] < b[index] ? -1 : 1));
         } else {
            return (+a[index] === +b[index] ? 0 : (+b[index] < +a[index] ? -1 : 1));
         }
      });
      $("#tr_table").html("");

      for (let i = from; i <= to; i++) {
         appendToTable(trlist[0][i]);
      }
}

function appendToTable(transaction) {
    var duration = transaction[1].toString();
    var hh = duration.substring(5,6)+"h";
    var mm = duration.substring(7,9)+"min";
    duration = hh + " " + mm;
    $("#tr_table").append(`
        <tr>
            <td>${transaction[0]}</td>
            <td>${duration}</td>
            <td>${transaction[2].toString().substring(0,10)}</td>
            <td>$${transaction[3]}</td>
            <td>$${transaction[4]}</td>
        </tr>
    `);
}
