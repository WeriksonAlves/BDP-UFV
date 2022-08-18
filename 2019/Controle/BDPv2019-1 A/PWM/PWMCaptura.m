switch PWM.B(1).String
    case 'Parar coleta'
        PWM.ObterDados = 0;
        plot(PWM.Pos(1,:),PWM.Pos(2,:),'parent',PWM.SegIm)
        axis ([-750 750 -650 650]);
        PWM.B(1).String='Obter dados';
    case 'Obter dados'
        PWM.B(1).String='Parar coleta';
        PWMColetarDados
end
