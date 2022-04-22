
switch PWM.B(1).String
    case'Parar coleta'
        PWM.B(1).String='Obter dados';
        PWM.ObterDados = 0;
end 

PWM.fileID = fopen(strcat(BDP.PathSystem,'\PWM\Testes\','PWM_',PWM.B(6).String,'_',PWM.B(7).String,'_(',PWM.B(5).String,')'),'wt');  
fprintf(PWM.fileID,'         X         Y\n');

for ii=1:size(PWM.Pos(1,:)')
    fprintf(PWM.fileID, '%10.3f %10.3f\n', PWM.Pos(1:2,ii));
end

fclose(PWM.fileID);

PWM.B(5).String = num2str(1+str2num(PWM.B(5).String));
