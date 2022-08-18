% ==================================================
% Desabilitar Botões
set(Campo.Botoes(:),'enable','on');

% ==================================================

% Colocar mensagem no log
set((BDP.status(1)),'string','Calibração do campo em validação')
set((BDP.status(2)),'string','Clique com botão direito para sair!')

axes(Campo.Real.ID)

while 1
    % Pixel de teste
    [Campo.Real.pxTeste(1),Campo.Real.pxTeste(2),Campo.Real.pxTeste(3)] = ginput(1);
    
    Campo.Padrao.pxTeste = PDI.T.transformPointsForward(Campo.Real.pxTeste(1:2));
    
    try 
        delete(Campo.Padrao.idPonto)
    end
    
    Campo.Padrao.idPonto = patch(Campo.Padrao.pxTeste(1)+25*cos(-pi:pi/6:pi),Campo.Padrao.pxTeste(2)+25*sin(-pi:pi/6:pi),[1 0 0],'parent',Campo.Padrao.ID);
        
    % Clicar com o botão direito
    if Campo.Real.pxTeste(3) == 3
        set(BDP.status(1),'string',' ')
        set(BDP.status(2),'string',' ')
        try
            delete(Campo.Padrao.idPonto)
        end
        break
    end
end


% ==================================================
% Habilitar Botões
set(Campo.Botoes(:),'enable','on');

