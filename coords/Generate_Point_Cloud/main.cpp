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

const char OUTPUT_NOISED_SPBR[] = "SPBR_DATA/square_coords-color_noise.spbr";

int main(int argc, char **argv) {
    if ( argc != 5 ) {
        std::cout << "USAGE  : " << argv[0] << " [num-of-points] [sigma4coords] [sigma4color] [probability-of-adding-noise]" << std::endl;
        std::cout << "EXAMPLE: " << argv[0] << " 1000000 0.01 40 0.1" << std::endl;
        exit(1);
    }

    // FILE open
    std::ofstream   fout;
    std::string     of_name( OUTPUT_NOISED_SPBR ); 
    fout.open( of_name );

    // Check args
    int num_of_points   = atoi(argv[1]);
    float sigma4coords  = atof(argv[2]);
    int sigma4color     = atoi(argv[3]);
    std::cout << "Number of points      : " << num_of_points << std::endl;
    std::cout << "sigma for coords noise: " << sigma4coords  << std::endl;
    std::cout << "sigma for color noise : " << sigma4color   << std::endl;

    // variables
    kvs::MersenneTwister        uniRand;
    std::vector<kvs::Vector3d>  plane_points;
    kvs::Vector3d               plane_point;
    double x, y, z; x = y = z = 0.0;
    kvs::BoxMuller  gaussRand;
    kvs::Vector3d   point;
    float probability_of_adding_noise = atof(argv[4]);
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
    std::cout << "\nAdding noise with " << probability_of_adding_noise*100 << "(%) ..." << std::endl;

    // Generate the point cloud
    for ( int i = 0 ; i < num_of_points; i++ ) {
        x = uniRand(); // random number [0...1] for x
        y = uniRand(); // random number [0...1] for y
        z = 0.0;

        // Noise points
        if ( i < num_of_points*probability_of_adding_noise ) {
            // Add coords noise
            z += gaussRand.rand(0, sigma4coords);
            noise_point_counter++;

            // Add color noise
            r_noised = g_noised = b_noised = gaussRand.rand(128, sigma4color);
            // if (r_noised < 0)    r_noised = 0;
            // if (r_noised > 255)  r_noised = 255;
            // if (g_noised < 0)    g_noised = 0;
            // if (g_noised > 255)  g_noised = 255;
            // if (b_noised < 0)    b_noised = 0;
            // if (b_noised > 255)  b_noised = 255;
            
            // Noise point
            fout << x        << " " << y        << " " << z         << " ";
            fout << 0        << " " << 0        << " " << 0         << " ";
            fout << r_noised << " " << g_noised << " " << b_noised  << "\n";

        // Original points
        } else {
            fout << x   << " " << y   << " " << z   << " ";
            fout << 0   << " " << 0   << " " << 0   << " ";
            fout << 255 << " " << 255 << " " << 255 << std::endl;
        } // end if

        // Show progress
        if ( (i+1) % int(num_of_points*0.1) == 0 ) {
            std::cout << (i*100)/num_of_points+1 << "\% done." << std::endl;
        }
    } // end for

    std::cout << "\nNumber of noise points"    << std::endl;
    std::cout << "> " << noise_point_counter << "\n"  << std::endl;  

    // FILE close
    fout.close();

    return 0;
}