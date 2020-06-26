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

const char OUTPUT_NOISED_SPBR[] = "SPBR_DATA/square_outlier-color-noise.spbr";

int main(int argc, char **argv) {
    if ( argc != 3 ) {
        std::cout << "USAGE  : " << argv[0] << " [num-of-points] [noise probability]" << std::endl;
        std::cout << "EXAMPLE: " << argv[0] << " 10000000 0.1" << std::endl;
        exit(1);
    }

    // FILE open
    std::ofstream   fout;
    std::string     of_name( OUTPUT_NOISED_SPBR ); 
    fout.open( of_name );

    // Check args
    int num_of_points       = atoi(argv[1]);
    float noise_probability = atof(argv[2]);
    std::cout << "Number of points      : " << num_of_points << " (points)" <<std::endl;
    std::cout << "Noise probability     : " << noise_probability*100  << " (%)" << std::endl;

    // variables
    kvs::MersenneTwister        uniRand;
    double x, y, z; x = y = z = 0.0;
    kvs::BoxMuller  gaussRand;
    int noise_point_counter = 0;
    int r_noised, g_noised, b_noised; r_noised = g_noised = b_noised = 0;

    // Set SPBR header
    fout << "#/SPBR_ASCII_Data"      << std::endl;
    fout << "#/RepeatLevel 1"        << std::endl;
    fout << "#/BGColorRGBByte 0 0 0" << std::endl;
    fout << "#/ImageResolution 512"  << std::endl;
    fout << "#/Shading 0"            << std::endl;
    fout << "#/LOD 0"                << std::endl;
    fout << "#/EndHeader"            << std::endl;

    // Stochastically, add noise to point cloud
    std::cout << "\nAdding outlier noise with " << noise_probability*100 << "(%) ..." << std::endl;

    // Generate noise model point cloud
    for ( int i = 0 ; i < num_of_points; i++ ) {
        x = uniRand(); // random number [0...1] for x
        y = uniRand(); // random number [0...1] for y
        z = 0.0;

        // Noise points
        if ( i < num_of_points*noise_probability ) {
            noise_point_counter++;

            // Add outlier noise to color (Grayscale)
            r_noised = g_noised = b_noised = int(uniRand()*255);
            
            // Noise point
            fout << x        << " " << y        << " " << z         << " ";
            fout << 0        << " " << 0        << " " << 0         << " ";
            fout << r_noised << " " << g_noised << " " << b_noised  << "\n";

        // Original points
        } else {
            fout << x   << " " << y   << " " << z   << " ";
            fout << 0   << " " << 0   << " " << 0   << " ";
            fout << 255 << " " << 255 << " " << 255 << "\n";
        } // end if

        // Show progress
        if ( (i+1) % int(num_of_points*0.1) == 0 ) {
            std::cout << (i*100)/num_of_points+1 << "\% done." << std::endl;
        }
    } // end for

    std::cout << "\nNumber of outlier noise points : " << noise_point_counter << "\n" << std::endl;  

    // FILE close
    fout.close();

    return 0;
}