classdef Adversario < handle
    % In a methods block, set the method attributes
    % and add the function signature
    properties
        
        % Properties or Parameters
        pCAD    % Pioneer 3DX 3D image
        pTime   % Time da equipe
        
        % Control variables
        pPos   % Posture
        pFlag  % Flags
    end
    
    methods
        function rBDP = Adversario()
            rBDP.pTime   = 'c';
            rBDP.pPos.X  = zeros(3,1);  % Postura atual
            iFlags(rBDP);
        end
        
        % ==================================================
        function iFlags(rBDP)
            % Indicar a criação do modelo CAD
            rBDP.pFlag.criado = 0;
        end
        
        % ==================================================
        function mCADplotar(rBDP,LocalImagem)
            if rBDP.pFlag.criado == 0
                rBDP.pFlag.criado = 1;
                % Exibição dos jogadores
                rBDP.pCAD.v    = [-35  35 35 -35; -35 -35 35 35;  1 1 1 1];
                rBDP.pCAD.id = patch(rBDP.pCAD.v(1,:),rBDP.pCAD.v(2,:),rBDP.pTime,'Parent',LocalImagem);
            else
                rBDP.pCAD.id.Vertices   = ([1 0 rBDP.pPos.X(1); 0 1 rBDP.pPos.X(2); 0 0 1]*rBDP.pCAD.v)';
            end
        end
    end
end