//----------------------------|
// on-the-fly synchronization
// adapted from Perry's ChucK Drummin' + Ge's sine poops
//
// authors: Perry Cook (prc@cs.princeton.edu)
//          Ge Wang (gewang@cs.princeton.edu)
// --------------------|          
// add one by one into VM (in pretty much any order):
// 
// terminal-1%> chuck --loop
// ---
// terminal-2%> chuck + otf_01.ck
// (anytime later)
// terminal-2%> chuck + otf_02.ck
// (etc...)
//--------------------------------------|

// synchronize to period
.5::second => dur T;
T - (now % T) => now;

// connect patch
SinOsc s => dac;
.25 => s.gain;

// scale (in semitones)
[7,5,3] @=> int scale[];

0 => int i;
// infinite time loop
while( true )
{
    i % scale.size() => i;
    // get note class
    scale[ i ] => float freq;
    // get the final freq    
    Std.mtof( 21.0 + (24.1 + freq) ) => s.freq;

    // advance time
    2::T => now;
    
    i++;
}
