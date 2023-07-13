% Identificação das cores
% 1- Red
% 2- Orange
% 3- Yellow
% 4- Green
% 5- Cyan
% 6- Blue
% 7- Magenta

% ============================================F
% Posicionar Bola
% Busca por maior área encontrada
if ~isempty(PDI.CoresMM)
    if ~isempty(PDI.CoresMM{2})
        [~,Bola.maxArea] = max(PDI.CoresMM{2}(:,3));
        Bola.Xa = Bola.X;
        Bola.X = PDI.CoresMM{2}(Bola.maxArea,1:2);
        Bola.dX = Bola.X - Bola.Xa;

        Bola3.X(1)= -750 + 25*cos(atan2((Bola.X(2)-0),(Bola.X(1)+750)));
        Bola3.X(2)= 200*sin(atan2((Bola.X(2)-0),(Bola.X(1)+750)));

        
    end
    % ============================================
    
    % Popular jogadores adversários
    % Determinar número de robôs adversários
    
    switch JogAdv(1).pTime
        % ============================================
        case 'y' % Yellow
            if ~isempty(PDI.CoresMM{3})
                for ii = 1:size(PDI.CoresMM{3},1)
                    JogAdv(ii).pPos.X = PDI.CoresMM{3}(ii,1:2)';
                end
            end
        case 'c' % Cyan
            if ~isempty(PDI.CoresMM{5})
                for ii = 1:size(PDI.CoresMM{5},1)
                    JogAdv(ii).pPos.X = PDI.CoresMM{5}(ii,1:2)';
                end
            end
            
    end
    
    for ii = 1:3
        switch JogBDP(ii).pTime
             
            % ============================================
            case 'y' % Yellow
                % Popular jogadores
                % Escolha da cor por proximidade
                if ~isempty(PDI.CoresMM{3})
                    switch JogBDP(ii).pCor
                        
                        case 'r' % Índice: 1
                            if ~isempty(PDI.CoresMM{1})
                                JogBDP(ii).pPos.Xa = JogBDP(ii).pPos.X;
                                JogBDP(ii).pPos.X = DeterminarProximidade(JogBDP(ii).pPos.X,PDI.CoresMM{3}(:,1:2),PDI.CoresMM{1}(:,1:2));
                                JogBDP(ii).pPos.dX = JogBDP(ii).pPos.X - JogBDP(ii).pPos.Xa;
%                                 JogBDP(ii).pPos.dX
%                                 ii
                            end
                        case 'g' % Índice: 4
                            if ~isempty(PDI.CoresMM{4})
                                JogBDP(ii).pPos.Xa = JogBDP(ii).pPos.X;
                                JogBDP(ii).pPos.X = DeterminarProximidade(JogBDP(ii).pPos.X,PDI.CoresMM{3}(:,1:2),PDI.CoresMM{4}(:,1:2));
                                JogBDP(ii).pPos.dX = JogBDP(ii).pPos.X - JogBDP(ii).pPos.Xa; 
                            end
                        case 'b' % Índice: 6
                            if ~isempty(PDI.CoresMM{6})
                                JogBDP(ii).pPos.Xa = JogBDP(ii).pPos.X;
                                JogBDP(ii).pPos.X = DeterminarProximidade(JogBDP(ii).pPos.X,PDI.CoresMM{3}(:,1:2),PDI.CoresMM{6}(:,1:2));
                                JogBDP(ii).pPos.dX = JogBDP(ii).pPos.X - JogBDP(ii).pPos.Xa; 
                            end
                        case 'm' % Índice: 7
                            if ~isempty(PDI.CoresMM{7})
                                JogBDP(ii).pPos.Xa = JogBDP(ii).pPos.X;
                                JogBDP(ii).pPos.X = DeterminarProximidade(JogBDP(ii).pPos.X,PDI.CoresMM{3}(:,1:2),PDI.CoresMM{7}(:,1:2));
                                JogBDP(ii).pPos.dX = JogBDP(ii).pPos.X - JogBDP(ii).pPos.Xa; 
                            end
                    end
                end
                
                % ============================================
            case 'c' % Cyan
                % Popular jogadores
                % Escolha da cor por proximidade
                if ~isempty(PDI.CoresMM{5})
                    switch JogBDP(ii).pCor
                        case 'r' % Índice: 1
                            if ~isempty(PDI.CoresMM{1})
                                JogBDP(ii).pPos.X = DeterminarProximidade(JogBDP(ii).pPos.X,PDI.CoresMM{5}(:,1:2),PDI.CoresMM{1}(:,1:2));
                            end
                        case 'g' % Índice: 4
                            if ~isempty(PDI.CoresMM{4})
                                JogBDP(ii).pPos.X = DeterminarProximidade(JogBDP(ii).pPos.X,PDI.CoresMM{5}(:,1:2),PDI.CoresMM{4}(:,1:2));
                                
                            end
                        case 'b' % Índice: 6
                            if ~isempty(PDI.CoresMM{6})
                                JogBDP(ii).pPos.X = DeterminarProximidade(JogBDP(ii).pPos.X,PDI.CoresMM{5}(:,1:2),PDI.CoresMM{6}(:,1:2));
                            end
                        case 'm' % Índice: 7
                            if ~isempty(PDI.CoresMM{7})
                                JogBDP(ii).pPos.X = DeterminarProximidade(JogBDP(ii).pPos.X,PDI.CoresMM{5}(:,1:2),PDI.CoresMM{7}(:,1:2));
                            end
                    end
                end
%                JogBDP(ii).pPos.dX = JogBDP(ii).pPos.X - JogBDP(ii).pPos.Xa; 
        end
    end
end

% =========================================================================
function Pos = DeterminarProximidade(Pos,A,B)
% Filtar por distância: D = 150mm
% Distância entre o centro do robô e sua camisa

id = [0 0];
D = 100;
for  ii = 1:size(A,1)
    for  jj = 1:size(B,1)
        d = norm(A(ii,1:2)-B(jj,1:2));
        if D > d
            D = d;
            id = [ii jj];
        end
    end
end

if sum(id) > 1
    % Posição do jogador
    Pos(1:2,1) = mean([A(id(1),1:2);B(id(2),1:2)])';
    
    % CORRIGIR: Singularidade entre -180 e 180
    % Orientação do jogador
%     if atan2(B(id(2),2)-A(id(1),2),B(id(2),1)-A(id(1),1)) <= pi

%     if Bola2.flag == 0 && (atan2(B(id(2),2)-A(id(1),2),B(id(2),1)-A(id(1),1))) < 0
%         psi = pi + abs(tan2(B(id(2),2)-A(id(1),2),B(id(2),1)-A(id(1),1))+pi);
%     else
%         psi = atan2(B(id(2),2)-A(id(1),2),B(id(2),1)-A(id(1),1))
%     end
% 
%     if JogBDP(1).pPar.flag == 1 && atan2(B(id(2),2)-A(id(1),2),B(id(2),1)-A(id(1),1)) > 0
%          psi = pi - abs(tan2(B(id(2),2)-A(id(1),2),B(id(2),1)-A(id(1),1)) - pi);
%     else
        psi = atan2(B(id(2),2)-A(id(1),2),B(id(2),1)-A(id(1),1));
%     end
%     if psi > pi/2
%         PDI_Flag == 0;
%     end
%     if psi < -pi/2
%         PDI_Flag == 1;
%     end
  
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %
    

    %
    Pos(3,1) = psi;
    %     if abs(psi - Pos(3,1)) > 5*pi/6
    %         Pos(3,1) =  2*pi*sign(Pos(3,1)) + psi;
    %     else
    %             Pos(3,1) = psi;
    %     end
    

    
end

end
