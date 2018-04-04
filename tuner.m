function tune = tuner(wav)
%---load note/frequency structure---
load('notes.mat');
%---read in wav file---
[y fs]= audioread(wav);
%---take fast fourier transform---
yft=fft(y);
%---take frequencies from sample rate---
freq=0:fs/length(y):fs/2;
%---reduce fft'd wave to half size---
if mod(length(y),2)==0
    ydft=yft(1:length(y)/2+1);
else
    ydft=yft(1:floor(length(y)/2)+1);
end
%---plot wave for lulz---
plot(freq,abs(ydft))
%---find max amplitude of fft'd wave---
[maxval, i]=max(abs(ydft));
%---find fundamental frequency---
% fundfreq = freq(i);
%---find index of the note freq closest to the fund freq---
[c index] = min(abs([note.freq]-freq(i)));
%---return note corresponding to frequency closest to fund freq---
tune=note(index).name;
end
