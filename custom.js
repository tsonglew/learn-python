/**
 * custom js
 */

(function(window, document) {
  var voteCount = 0;
  var $checkboxes = $("input[type='checkbox']");
  var form = $('#voteForm');
  $checkboxes.click(checkVote);
  var voteCount = 0;

  function checkVote() {
    voteCount = 0;
    for (var i = 0; i < $checkboxes.length; i++) {
      if ($checkboxes.eq(i).is(':checked')) {
        voteCount += 1;
      }
    }
    if (voteCount == 3) {
      for (var i = 0; i < $checkboxes.length; i++) {
        if (!$checkboxes.eq(i).is(':checked')) {
          $checkboxes.eq(i).attr("disabled", true);
        }
      }
    } else {
      $checkboxes.removeAttr("disabled");
    }
  }

  function setCookie(name, value) {
    var Days = 30;
    var exp = new Date();
    exp.setTime(exp.getTime() + Days * 24 * 60 * 60 * 1000);
    document.cookie = name + "=" + escape(value) + ";expires=" + exp.toGMTString();
  }

  function getCookie(name) {
    var arr, reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");
    if (arr = document.cookie.match(reg))
      return unescape(arr[2]);
    else
      return null;
  }

  $('#voteForm').submit(function(e) {
		if (getCookie('voted')){
			e.preventDefault();
			alert('您已经投过票了！');
		}else if(voteCount < 3){
      e.preventDefault();
      alert('请选择三位候选人！');	
		}else{
      setCookie('voted', 1)
    }
  })
})(window, document);
