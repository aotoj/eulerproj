!ams129/../project/fortran/main.F90!
!---------------------------!
!Joel Aoto                  !
!AMS129, MWF 9:20pm         !
!project: euler.F90         !
!---------------------------!

program main
use euler, only: eulers_method
implicit none

        integer :: t_0, y_0, t_f
        CHARACTER (len = 2):: eight, sixt,three2,six4
        t_0 = 0
        y_0 = -2
        t_f = 10
        eight = '8'
        sixt = '16'
        three2 = '32'
        six4 = '64'
        
        call eulers_method(t_0, t_f, y_0, 8, eight)
        call eulers_method(t_0, t_f, y_0, 16, sixt)
        call eulers_method(t_0, t_f, y_0, 32, three2)
        call eulers_method(t_0, t_f, y_0, 64, six4)



end program main
