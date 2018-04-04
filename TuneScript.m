%--initialize recorder object--
recObj = audiorecorder;
disp('tuner on')
%---loop as long as user wants---
while true
recordblocking(recObj,.1); %--record 10 samples/sec
data=getaudiodata(recObj);
disp(realTimeTuner(data,8000));
end