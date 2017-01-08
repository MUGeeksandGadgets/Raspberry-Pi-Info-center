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
            var ampm = h >= 12 ? 'pm' : 'am';
            h = h % 12; // correcting for AM PM
            h = h ? h : 12; // the hour '0' should be '12'
            document.getElementById('clock').innerHTML=h + ":" + m + " " + ampm;
            time = setTimeout('startClock()',500); // this keeps the clock rolling
        }

        function checkTime(i){
            if (i<10){
                i="0" + i;
            }
            return i;
         }