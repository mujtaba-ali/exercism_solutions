"
" This function takes a year and returns 1 if it's a leap year
" and 0 otherwise.
"
function! LeapYear(year) abort

  " your implementation goes here
  if year % 4 == 0
  {
      if year % 100 == 0 && year % 400 == 0{
          return 1;
      }    
      else if year % 100 == 0{
         return 0;
      }  
      return 1;
  end if
 }
 endif
 return 0;

endfunction
