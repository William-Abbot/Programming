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
.3 => s.gain;

// scale (in semitones)
[ 0, 2, 4, 7, 9, 12] @=> int scale[];
[ -1, 1, 3, 6, 8, 10] @=> int scale2[];

0 => int i;
// infinite time loop
while( true )
{
    for( 0 => int j; j < 18; j++)
    {
        i % scale.size() => i;
        // get note class
        scale[ i ] => float freq;
        // get the final freq    
        Std.mtof( 21.0 + (36 + freq) ) => s.freq;

        // advance time
        0.5::T => now;
        i++;
    }
    0 => i;
    for( 0 => int j; j < 12; j++)
    {
        i % scale.size() => i;
        // get note class
        scale2[ i ] => float freq;
        // get the final freq    
        Std.mtof( 21.0 + (36 + freq) ) => s.freq;

        // advance time
        0.5::T => now;
        i++;
    }
}
