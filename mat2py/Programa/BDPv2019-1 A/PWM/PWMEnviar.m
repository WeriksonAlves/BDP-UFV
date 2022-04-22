
switch PWM.B(4).Value
    case 1
        COM.msg = ['B' 'D' 150+str2num(PWM.B(6).String) 150+str2num(PWM.B(7).String) 150 150 150 150, 'P' 10];
    case 2
        COM.msg = ['B' 'D' 150 150 150+str2num(PWM.B(6).String) 150+str2num(PWM.B(7).String) 150 150, 'P' 10];
    case 3
        COM.msg = ['B' 'D' 150 150 150 150 150+str2num(PWM.B(6).String) 150+str2num(PWM.B(7).String), 'P' 10];
end

fwrite(COM.Porta,COM.msg,'char');




