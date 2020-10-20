!ams129/../project/fortran/euler.F90!
!---------------------------!
!Joel Aoto                  !
!AMS129, MWF 9:20pm         !
!project: euler.F90         !
!---------------------------!
module euler
        implicit none
        real, external:: dydt
        contains

        subroutine eulers_method(t_0, t_f, y_0, N, file_num)
                integer, intent(in):: t_0,y_0, t_f, N
                character (len = 2), intent(in):: file_num                
                CHARACTER (len=200):: file_name
                real :: t_n, y_n, f_nn, y_nn, h, m
                integer :: i
                y_n = y_0
                file_name = 'output_'//file_num//'.txt'
                m = N
                open(unit=100, file= file_name)
                write(100, *) '                  t_n     ', '                   y'                
                do i = 0,N
                h = abs(t_f - t_0)/(m)
                t_n = t_0 + i*h

                f_nn = dydt(t_n, y_n)
                y_nn = y_n + f_nn*h
                y_n = y_nn

                if ( N == 8) then
                write(100, *) t_n, y_nn
                else if (N == 16) then
                write(100, *) t_n, y_nn
                else if (N == 32) then
                write(100, *) t_n, y_nn
                else if (N == 64) then
                write(100, *) t_n, y_nn
                end if
                end do
                close(100)
                
        end subroutine eulers_method
     
end module euler

real function dydt(t,y)
        real, intent(in):: t,y
        dydt = (2*t)/(y*(1+t**2))
end function dydt
