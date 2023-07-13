% ==================================================
% Desabilitar Botões
set(Campo.Botoes(:),'enable','off');

% ==================================================

% Indicação dos pontos no campo padrão

axes(Campo.Real.ID)
Campo.Real.idPontos = [];

for ii = 1:length(Campo.Padrao.idPontos)
    try 
        delete(Campo.Padrao.idTexto)
        delete(Campo.Padrao.idPonto)
    end
    
    Campo.Padrao.idTexto = text(Campo.Padrao.idPontos(ii,1)+50,Campo.Padrao.idPontos(ii,2),num2str(ii),'color','r','fontsize',20,'parent',Campo.Padrao.ID);
    Campo.Padrao.idPonto = patch(Campo.Padrao.idPontos(ii,1)+25*cos(-pi:pi/6:pi),Campo.Padrao.idPontos(ii,2)+25*sin(-pi:pi/6:pi),[1 0 0],'parent',Campo.Padrao.ID);
    
    % Capturar a posição na imagem referente ao ponto do Campo Padrão
    Campo.Real.idPontos(ii,:) = ginput(1);
    
    delete(Campo.Padrao.idTexto)
    delete(Campo.Padrao.idPonto)
end

% Obter transformação de projectiva entre a câmera e o campo padrão
PDI.T = fitgeotrans(Campo.Real.idPontos,Campo.Padrao.idPontos,'projective');

% Criar campo padrão sobre a campo real
try
    delete(Campo.Real.mm2px)
end
for ii = 1:4
    Campo.Real.px(:,:,ii) = PDI.T.transformPointsInverse(Campo.Padrao.XY(1:2,:,ii+1)');
    Campo.Real.mm2px(ii)  = patch(Campo.Real.px(:,1,ii),Campo.Real.px(:,2,ii),[0 0 0],'Parent',Campo.Real.ID,'EdgeColor',[1 0 0],'FaceAlpha',0,'EdgeAlpha',0.5);
    
end

% ==================================================
% Habilitar Botões
set(Campo.Botoes(:),'enable','on');