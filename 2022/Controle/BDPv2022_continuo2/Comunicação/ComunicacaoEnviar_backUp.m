% Somar 100 para casos de valores negativos

%  COM.msg = ['B' 'D' 22 uint8(JogBDP(1).pSC.PWM') uint8(JogBDP(2).pSC.PWM')+16 uint8(JogBDP(3).pSC.PWM')+16 'P'];
% COM.msg = ['B' 'D' 22 116 116 116 116 116 116 'P'];
% % % % %  COM.msg = ['B' 'D' uint8(JogBDP(1).pSC.PWM'+150) uint8(JogBDP(2).pSC.PWM'+150) uint8(JogBDP(3).pSC.PWM'+150) 'P' 10];
 
%%
% % % % % % if JogBDP(1).pFuncao == 'a'
% % % % %     if sqrt( (JogBDP(1).pPos.X(2,1) - Bola2.X(2))^2 + (JogBDP(1).pPos.X(1,1) - Bola2.X(1))^2 ) > 150  && abs(ang_dif) > 10
% % % % %         ang  = atan2(Bola2.X(2)-JogBDP(1).pPos.X(2,1),(Bola2.X(1)-JogBDP(1).pPos.X(1,1)));
% % % % %         Bola.Status = 1;   
% % % % %     else
% % % % %         ang  = atan2(Bola.X(2)-JogBDP(1).pPos.X(2,1),(Bola.X(1)-JogBDP(1).pPos.X(1,1)));
% % % % %         Bola.Status = 0; 
% % % % %     end
% % % % %     
% % % % %     
% % % % %     if abs(ang) > pi
% % % % %         if ang > 0 
% % % % %             ang = ang - 2*pi;
% % % % %         else
% % % % %             ang = ang + 2*pi;
% % % % %         end
% % % % %     end
% % % % %     
% % % % %     
% % % % %     
% % % % %     ang = rad2deg(ang);
% % % % %     ang_dif = ang - rad2deg(JogBDP(1).pPos.X(3,1));
% % % % %     
% % % % %     
% % % % %     if abs(ang_dif) > 180
% % % % %         if ang_dif > 0 
% % % % %             ang_dif = ang_dif - 2*180;
% % % % %         else
% % % % %             ang_dif = ang_dif + 2*180;
% % % % %         end
% % % % %     end
% % % % %     
% % % % %     % if abs(ang-ang_dif)< 10
% % % % %     %     if ang-ang_dif>0
% % % % %     %         ang_dif = ang_dif + 25;
% % % % %     %         disp('entrou+')
% % % % %     %     else
% % % % %     %         ang_dif = ang_dif - 25;
% % % % %     %         disp('entrou-')
% % % % %     %     end
% % % % %     % end
% % % % %     
% % % % %     % disp(['ang =' num2str(ang)]);
% % % % %     % COM.msg = ['B' 'D' 150 150 150 150 150 150 'P' 10];
% % % % %     
% % % % %     if ang_dif> 15
% % % % %      COM.msg = ['B' 'D' 150 150 150 150 143 158 'P' 10];%roda antihorario
% % % % %     %   disp(['COM.msg =' num2str(round(ang/2)),' 0']);
% % % % %     
% % % % %     
% % % % %     elseif ang_dif < -15
% % % % %       COM.msg = ['B' 'D' 150 150  150 150 158 143 'P' 10];%roda horario
% % % % %     %   disp(['COM.msg = 0 ', num2str(abs(round(ang/2))+150)]);
% % % % %     
% % % % %       
% % % % %     else
% % % % %        COM.msg = ['B' 'D' 150 150 130 130 150+5 150+5 'P' 10];
% % % % %        JogBDP(1).pPar.avanca = JogBDP(1).pPar.avanca + 1;
% % % % %        JogBDP(1).pPar.ctr_avanca = 1;
% % % % %                 borda = 0;
% % % % %     
% % % % %     end
% % % % %     
% % % % %     
% % % % %     if JogBDP(1).pPar.ctr_avanca == 1 && JogBDP(1).pPar.avanca > 3
% % % % %         JogBDP(1).pPar.avanca = 0;
% % % % %         JogBDP(1).pPar.ctr_avanca = 0;
% % % % %          borda = 0;
% % % % %     
% % % % %     end
% % % % %     
% % % % %     
% % % % %     if JogBDP(1).pPar.ctr_avanca == 1 && JogBDP(1).pPar.avanca == 2 
% % % % %          COM.msg = ['B' 'D' 150 150 150 150 150+100 150+100 'P' 10];
% % % % %         JogBDP(1).pPar.avanca = JogBDP(1).pPar.avanca + 1;
% % % % %     
% % % % %     end
% % % % %     
% % % % %     if JogBDP(1).pPar.avanca == 1 
% % % % %          COM.msg = ['B' 'D' 150 150 150 150 150+20 150+25 'P' 10];
% % % % %         JogBDP(1).pPar.ctr_avanca = 1;
% % % % %         JogBDP(1).pPar.avanca = JogBDP(1).pPar.avanca + 1;
% % % % %     
% % % % %     end
% % % % %     
% % % % %     if abs(JogBDP(1).pPos.X(2)) > 620 || (abs(JogBDP(1).pPos.X(1)) > 500 && abs(JogBDP(1).pPos.X(2)) < 620) 
% % % % %         borda = 1 + borda;
% % % % %     else
% % % % %         borda = 0;
% % % % %     end
% % % % %     
% % % % %     
% % % % %     
% % % % %     if borda > 25
% % % % %              COM.msg = ['B' 'D' 150 150 170 170 150+140 150-145 'P' 10];
% % % % %              borda = 0;
% % % % %              disp('BORDOU')
% % % % %     end
% % % % % end
% % % % % 
% % % % % 
% % % % % %%
% % % % % %  COM.msg = ['B' 'D' 200 150 150 150 150 150 'P' 10];%reto
% % % % % % if JogBDP(1).pFuncao == 'g'
% % % % % %         ang  = atan2(Bola3.X(2)-JogBDP(1).pPos.X(2,1),(Bola3.X(1)-JogBDP(1).pPos.X(1,1)));
% % % % % %     
% % % % % %     
% % % % % %     if abs(ang) > pi
% % % % % %         if ang > 0 
% % % % % %             ang = ang - 2*pi;
% % % % % %         else
% % % % % %             ang = ang + 2*pi;
% % % % % %         end
% % % % % %     end
% % % % % %     
% % % % % %     
% % % % % %     
% % % % % %     ang = rad2deg(ang);
% % % % % %     ang_gole = ang - rad2deg(JogBDP(1).pPos.X(3,1));
% % % % % %     
% % % % % %     
% % % % % %     if abs(ang_gole) > 180
% % % % % %         if ang_gole > 0 
% % % % % %             ang_gole= ang_gole - 2*180;
% % % % % %         else
% % % % % %             ang_gole = ang_gole + 2*180;
% % % % % %         end
% % % % % %     end
% % % % % %     JogBDP(1).dGoleBol = sqrt( (JogBDP(1).pPos.X(2,1) - Bola3.X(2))^2 + (JogBDP(1).pPos.X(1,1) - Bola3.X(1))^2 );
% % % % % %     JogBDP(1).dGoleP = sqrt( (JogBDP(1).pPos.X(2,1) - Bola.X(2))^2 + (JogBDP(1).pPos.X(1,1) - Bola.X(1))^2 );
% % % % % %  
% % % % % %   if JogBDP(1).dGoleBol> 60
% % % % % %        
% % % % % %     if ang_gole> 15
% % % % % %      COM.msg = ['B' 'D' 160 160 160 160 150 150 'P' 10];%roda antihorario
% % % % % %     %   disp(['COM.msg =' num2str(round(ang/2)),' 0']);
% % % % % %     
% % % % % %     
% % % % % %     elseif ang_gole < -15
% % % % % %       COM.msg = ['B' 'D' 100 100 140 140 150 150 'P' 10];%roda horario
% % % % % %     %   disp(['COM.msg = 0 ', num2str(abs(round(ang/2))+150)]);
% % % % % %     
% % % % % %       
% % % % % %     else
% % % % % %        COM.msg = ['B' 'D' 140 143 150-10 150+15 150 150 'P' 10];
% % % % % %     end
% % % % % %         
% % % % % %   else
% % % % % % %         COM.msg = ['B' 'D' 150 150 150 150 150 150 'P' 10];
% % % % % %        if JogBDP(1).dGoleP <= 300 && Bola.X(2) > 0;
% % % % % %              COM.msg = ['B' 'D' 100 100 150-140 150-145 150 150 'P' 10];
% % % % % %        end
% % % % % %        if JogBDP(1).dGoleP <= 300 && Bola.X(2) < 0;
% % % % % %              COM.msg = ['B' 'D' 100 100  150+145 150-140 150 150 'P' 10];
% % % % % %        end
% % % % % %    end
% % % % % % end
%%

  COM.msg = ['B' 'D' 150+round(JogBDP(1).pSC.PWM') 150+round(JogBDP(2).pSC.PWM') 150+round(JogBDP(3).pSC.PWM') 'P' 10];
% 
%    COM.msg = ['B' 'D' 150 150 250 250 250 250 'P' 10];
 fwrite(COM.Porta,COM.msg,'char');
 disp(uint8(COM.msg(3:8)));

% edicao hiago
if toc(t_debug) - debugTime > 10 % A cada 10s verifica a perda de pacote
    Loss = char2array(fscanf(COM.Porta, '%c'));
    disp(Loss)
    debugTime = toc(t_debug);
end
