classdef Patola < handle
    % In a methods block, set the method attributes
    % and add the function signature
    properties
        
        % Properties or Parameters
        pCAD    % Pioneer 3DX 3D image
        pTime   % Time da equipe
        pCor    % Cor da camisa
        pFuncao % Função em campo
        pLado   % Lado de ataque
        pPar    % Parameters
        
        % Control variables
        pPos   % Posture
        pSC    % Signals
        pFlag  % Flags
        
        % Navigation Data and Communication
        pData % Flight Data
        pCom  % Communication
        
    end
    
    methods
        function rBDP = Patola()
            iFlags(rBDP);
            iDadosIniciais(rBDP);
            iVariaveisControle(rBDP);
        end
        
        % ==================================================
        iFlags(rBDP);
        iDadosIniciais(rBDP);
        iVariaveisControle(rBDP);
        
        % ==================================================
        % Imagem
        mCADplotar(rBDP,LocalImagem)
        
        % ==================================================
        % Command
        % rEnviarSinaisControle(rBDP);
        
    end
end