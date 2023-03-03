   function updateChars(){  
    alert("TESTING")
   }  

   function setNumLetters(e) {
      for (var t = document.querySelectorAll("input[name^='word']"), n = t.length, o = 0; o < n; o++) t[o].style.display = o < e ? "" : "none"
    }

    if (document.getElementById('no_of_letters')) {
      var num = document.getElementById('no_of_letters').value;
      setNumLetters(num);
      document.getElementById('no_of_letters').addEventListener('change', function() {
        console.log('changed');
        var num = parseInt(document.getElementById('no_of_letters').value);
        setNumLetters(num);
      });
      document.getElementById('solverform').addEventListener('submit', function() {
        var num = document.getElementById('no_of_letters').value;
        var searchstr = '';
        var inps = document.querySelectorAll('#solverform input.textbox');
        var ninps = inps.length;
        for (var i = 0; i < ninps; i++) {
          var curinp = inps[i];
          if (i < num) {
            if (curinp.value == '') {
              searchstr += '-';
            } else {
              searchstr += curinp.value.toLowerCase();
            }
            console.log(searchstr)
          }
        }
        window.location = '/solve/' + searchstr;
        return false;
      });}

      document.getElementById("solverform").addEventListener("submit", function() {
         for (var e = document.getElementById("no_of_letters").value, t = "", n = document.querySelectorAll("#solverform input.textbox"), o = n.length, r = 0; r < o; r++) {
           var a = n[r];
           r < e && ("" == a.value ? t += "-" : t += a.value.toLowerCase())
         }
         return window.location = "/solve/" + t, !1
       })

