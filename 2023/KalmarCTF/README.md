# KalmarCTF 2023
## Rev
1. CycleChaser

I used to chase cycles, but I got bored so I switched direction.
nc 3.123.91.129 13339

2. Works on my machine

hmmm it runs on my machine, but I don't quite get why the use of udbgwr instruction in the initialization phase. Intel Docs is really vague on this instruction can you help me

3. CycleChaser Revenge

You've solved the warmup! This time you will have to jump through some hoops.
nc 3.123.91.129 13340 

4. Jumping on the PPU

I found an old blu-ray disc with a game on it so I decided to dump it, can you find anything interesting inside of it? (If you find a flag and it doesn't work, try the other challenge!)

5. Jumping on the SPU

I found an old blu-ray disc with a game on it so I decided to dump it, can you find anything interesting inside of it? (If you find a flag and it doesn't work, try the other challenge!)

## Pwn
1. mjs

Toddler's first browser exploitation: https://github.com/cesanta/mjs
nc 54.93.211.13 10002 

2.  js in my bs 

Who doesn't need a JS engine in their boot sector? Am I right?

> a=1+1

> b=2+2

> l(a+b)

0006

There are multiple steps to the challenge, but the entire thing can be solved from within QEMU and does not require any mode switching.
nc 54.93.211.13 10000 

3. swedish Memcpy

Yet another OSDev challenge. Hope you've brought a copy of Intel® 64 and IA-32 Architectures Software Developer's Manual!

f you get messages like Invalid data, try running stty -icanon before connecting and if that fails, try a different terminal emulator. source: https://stackoverflow.com/questions/30315957/string-from-input-is-limited
nc 54.93.211.13 10001 

4. hyper-k

It's all about infra and kalmar will be the new big cloud provider in town, Silicon valley here we go, TO THE MOOON!

This chall is HARD (I think). It requires intel vt-x sorry if you're on amd. We have special infra for this chall and we will do our best to assist you if shit breaks. If everything fails contact zanderdk and we may be able to provide you with a private instance for a suitable region. Timeout etc should not be a issue so contact if you have such problems.

Best of luck Zander
nc 130.61.225.80 1337 

5. Robber

My friend Rob the robber sent me this file talking about this ground-breaking technique called rob?
nc 54.93.211.13 10004 

