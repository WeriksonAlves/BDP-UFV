% Somar 100 para casos de valores negativos

%  COM.msg = ['B' 'D' 22 uint8(JogBDP(1).pSC.PWM') uint8(JogBDP(2).pSC.PWM')+16 uint8(JogBDP(3).pSC.PWM')+16 'P'];
% COM.msg = ['B' 'D' 22 116 116 116 116 116 116 'P'];
% % % % %  COM.msg = ['B' 'D' uint8(JogBDP(1).pSC.PWM'+150) uint8(JogBDP(2).pSC.PWM'+150) uint8(JogBDP(3).pSC.PWM'+150) 'P' 10];
 

if sqrt( (JogBDP(1).pPos.X(2,1) - Bola2.X(2))^2 + (JogBDP(1).pPos.X(1,1) - Bola2.X(1))^2 ) > 150%% && abs(ang_dif) < 10
    ang  = atan2(Bola2.X(2)-JogBDP(1).pPos.X(2,1),(Bola2.X(1)-JogBDP(1).pPos.X(1,1)));
    Bola.Status=1;%tem o 2 tb
else
    ang  = atan2(Bola.X(2)-JogBDP(1).pPos.X(2,1),(Bola.X(1)-JogBDP(1).pPos.X(1,1)));
end


if abs(ang) > pi
    if ang > 0 
        ang = ang - 2*pi;
    else
        ang = ang + 2*pi;
    end
end

ang = rad2deg(ang);
ang_dif = ang - rad2deg(JogBDP(1).pPos.X(3,1));


if abs(ang_dif) > 180
    if ang_dif > 0 
        ang_dif = ang_dif - 2*180;
    else
        ang_dif = ang_dif + 2*180;
    end
end



% disp(['ang =' num2str(ang)]);
% COM.msg = ['B' 'D' 150 150 150 150 150 150 'P' 10];

if ang_dif> 15
 COM.msg = ['B' 'D' 100 100 160 160 150 150 'P' 10];%roda antihorario
%   disp(['COM.msg =' num2str(round(ang/2)),' 0']);


elseif ang_dif < -15
  COM.msg = ['B' 'D' 100 100 140 140 150 150 'P' 10];%roda horario
%   disp(['COM.msg = 0 ', num2str(abs(round(ang/2))+150)]);

  
else
   COM.msg = ['B' 'D' 100 100 150-10 150+15 150 150 'P' 10];
   JogBDP(1).pPar.avanca = JogBDP(1).pPar.avanca + 1;
   JogBDP(1).pPar.ctr_avanca = 1;
            borda = 0;

end


if JogBDP(1).pPar.ctr_avanca == 1 && JogBDP(1).pPar.avanca > 3
    JogBDP(1).pPar.avanca = 0;
    JogBDP(1).pPar.ctr_avanca = 0;
     borda = 0;

end


if JogBDP(1).pPar.ctr_avanca == 1 && JogBDP(1).pPar.avanca == 2 
     COM.msg = ['B' 'D' 100 100 150-100 150+100 150 150 'P' 10];
    JogBDP(1).pPar.avanca = JogBDP(1).pPar.avanca + 1;
disp('daniel gay')
end

if JogBDP(1).pPar.avanca == 1 
     COM.msg = ['B' 'D' 100 100 150-20 150+25 150 150 'P' 10];
    JogBDP(1).pPar.ctr_avanca = 1;
    JogBDP(1).pPar.avanca = JogBDP(1).pPar.avanca + 1;
disp(' gay')
end

if abs(JogBDP(1).pPos.X(2)) > 620 || (abs(JogBDP(1).pPos.X(1)) > 500 && abs(JogBDP(1).pPos.X(2)) < 620) 
    borda = 1 + borda;
else
    borda = 0;
end



if borda > 25
         COM.msg = ['B' 'D' 100 100 150-140 150-145 150 150 'P' 10];
         borda = 0;
         disp('BORDOU')
end

     
    

 %COM.msg = ['B' 'D' 150 150 150-10 150+15 150 150 'P' 10];%reto

fwrite(COM.Porta,COM.msg,'char');


