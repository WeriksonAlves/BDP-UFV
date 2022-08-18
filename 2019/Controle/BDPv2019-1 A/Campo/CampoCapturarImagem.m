% TESTE PDI
% Campo.Real.Im  = imresize(imread('img13.png'),Cam.Redimensionar,'bicubic');

if Cam.Redimensionar == 1
    Campo.Real.Im  = flipud(getsnapshot(Cam.Video));
else
    Campo.Real.Im  = flipud(imresize(getsnapshot(Cam.Video),Cam.Redimensionar));
end
Campo.Real.fig = imshow(Campo.Real.Im,'parent',Campo.Real.ID);

% Criar campo padrão sobre a campo real
try
    delete(Campo.Real.mm2px)
    
    for ii = 1:4
        Campo.Real.px(:,:,ii) = PDI.T.transformPointsInverse(Campo.Padrao.XY(1:2,:,ii+1)');
        Campo.Real.mm2px(ii)  = patch(Campo.Real.px(:,1,ii),Campo.Real.px(:,2,ii),[0 0 0],'Parent',Campo.Real.ID,'EdgeColor',[1 0 0],'FaceAlpha',0,'EdgeAlpha',0.5);
    end
    
end