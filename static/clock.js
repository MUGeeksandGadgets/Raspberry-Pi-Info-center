/**
 * Created by neo on 1/8/17.
 */
function startClock(){
            var today = new Date();
            var h = today.getHours();
            var m = today.getMinutes();
            // add a zero in front of numbers<10
            m = checkTime(m);
            h = checkTime(h);
            document.getElementById('clock').innerHTML=h+":"+m;
            time = setTimeout('startClock()',500);
        }

        function checkTime(i){
            if (i<10){
                i="0" + i;
            }
            return i;
         }