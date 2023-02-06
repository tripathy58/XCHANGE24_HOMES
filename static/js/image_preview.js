$(document).ready(function () {
    if (window.File && window.FileList && window.FileReader) {
      $("#files").on("change", function (e) {
        var files = e.target.files,
          filesLength = 10;
          
        for (var i = 0; i < filesLength; i++) {
          var f = files[i]
          var fileReader = new FileReader();
          fileReader.onload = (function (e) {
            var dvPreview = $("[id*=dvPreview]");
            var file = e.target;
            // $("<br/><br/><div style=\"display:flex !important;\">" +
            // "<div   class=\"pip\">" +
            //   "<img style=\"height:60px;\ width:80px\" class=\"imageThumb\" src=\"" + e.target.result + "\" title=\"" + file.name + "\"/>" +
            //   "<br/><span class=\"remove\">Remove image</span>" +
            //   "</div>"+
            //   "</div>").insertAfter("#files");
            // $(".remove").click(function () {
            //   $(this).parent(".pip").remove();
            // });
            var file = $("<img />");
                                  file.attr("style", "height:70px;width: 70px");
                                  file.attr("src", e.target.result);
                                  var div = $("<div style='float:left;' />");
                                  $(div).html("<span style='float:right;background-color:red;border-radius:50%;height:15px;width:15px;color:white;text-align:center;cursor:pointer;margin-top:-5px;' class='closeDiv'>X<span>");
                                  div.append(file);
            
                                  dvPreview.append(div);
          });
          fileReader.readAsDataURL(f);
        }
      });
    } else {
      alert("Your browser doesn't support to File API")
    }
  });
  $('body').on('click', '.closeDiv', function () {
          $(this).closest('div').remove();
      });
    


// $(function () {
//   $('[id*=fuUpload1]').change(function () {
//       if (typeof (FileReader) != "undefined") {
//           var dvPreview = $("[id*=dvPreview]");
//           var regex = /^([a-zA-Z0-9\s_\\.\-:])+(.jpg|.jpeg|.gif|.png|.bmp)$/;
//           $($(this)[0].files).each(function () {
//               var file = $(this);
//               if (regex.test(file[0].name.toLowerCase())) {
//                   var reader = new FileReader();
//                   reader.onload = function (e) {
//                       var img = $("<img />");
//                       img.attr("style", "height:100px;width: 80px");
//                       img.attr("src", e.target.result);
//                       var div = $("<div style='float:left;' />");
//                       $(div).html("<span style='float:right;background-color:red;border-radius:50%;height:15px;width:15px;color:white;text-align:center;cursor:pointer;margin-top:-5px;' class='closeDiv'>X<span>");
//                       div.append(img);

//                       dvPreview.append(div);
//                   }
//                   reader.readAsDataURL(file[0]);
//               } else {
//                   alert(file[0].name + " is not a valid image file.");
//                   dvPreview.html("");
//                   return false;
//               }
//           });
//       } else {
//           alert("This browser does not support HTML5 FileReader.");
//       }
//   });

//   $('body').on('click', '.closeDiv', function () {
//       $(this).closest('div').remove();
//   });
// });

 

  



  