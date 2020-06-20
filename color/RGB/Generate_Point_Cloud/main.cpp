#include <kvs/BoxMuller>
#include <kvs/MersenneTwister>
#include <kvs/Vector3>
#include <kvs/ColorMap>
#include <iostream>
#include <fstream>
#include <cstring> 
#include <cstdlib>
#include <cmath>
#include <vector>
#include <math.h>

#define  N_TOTAL      10000000
#define  TRUTH_MAX    0.99
#define  TRUTH_MIN    0.01

const char OUTPUT_FILE_NAME[] = "SPBR_DATA/plane_red_color_noise.spbr";

int main(int argc, char **argv) {
    if ( argc != 2 ) {
        std::cout << "USAGE: " << argv[0] << " [Num. of points]" << std::endl;
        exit(1);
    }

    // FILE open
    std::ofstream   fout;
    std::string     of_name( OUTPUT_FILE_NAME ); 
    fout.open( of_name );

    int num_of_points = atoi(argv[1]);
    std::cout << "Number of points: " << num_of_points << std::endl;

    // Set SPBR header
    fout << "#/SPBR_ASCII_Data"      << std::endl;
    fout << "#/RepeatLevel 1"        << std::endl;
    fout << "#/BGColorRGBByte 0 0 0" << std::endl;
    fout << "#/ImageResolution 512"  << std::endl;
    fout << "#/Shading 0"            << std::endl;
    fout << "#/LOD 0"                << std::endl;
    fout << "#/EndHeader"            << std::endl;

    // Variables
    kvs::MersenneTwister        uniRand;
    kvs::BoxMuller              gaussRand;
    double x, y, z; x = y = z = 0.0;
    int r, g, b; r = g = b = 255;

    // Add Gaussian noise to "color" of all 3D points.
    for ( int i = 0 ; i < num_of_points; i++ ) {
        x = uniRand(); // random number [0...1] for x
        y = uniRand(); // random number [0...1] for y
        z = 0.0;

        // N(μ, σ)
        // N(0, 1) → μ=0, σ=1

        // Add red noise
        if (i < num_of_points*0.1) { 
            r = 255; g = 0; b = 0; // Red 
        } else {
            r = g = b = 255; // White
        } // end if

        // Write to .spbr file 
        fout << x << " " << y << " " << z << " ";
        fout << 0 << " " << 0 << " " << 0 << " ";
        fout << r << " " << g << " " << b << "\n";

        // Show progress
        if ( (i+1) % int(num_of_points*0.1) == 0 ) {
            std::cout << (i*100)/num_of_points+1 << "\% done." << std::endl;
        }
    } // end for

    // FILE close
    fout.close();

    return 0;
}