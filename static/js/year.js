$(function () {
    $('#datepicker').datepicker({
      changeYear: true,
      showButtonPanel: true,
      dateFormat: 'yy',
      onClose: function (dateText, inst) {
        var year = $("#ui-datepicker-div .ui-datepicker-year :selected").val();
        $(this).datepicker('setDate', new Date(year, 1));
      }
    });

    $("#datepicker").focus(function () {
      $(".ui-datepicker-month").hide();
      $(".ui-datepicker-calendar").hide();
    });

  });