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

const char OUTPUT_FILE_NAME[] = "SPBR_DATA/plane_color_noise.spbr";

int main(int argc, char **argv) {
    if ( argc != 4 ) {
        std::cout << "USAGE: " << argv[0] << " [Num. of points] [C_pt] [sigma2(variance)]" << std::endl;
        exit(1);
    }

    // FILE open
    std::ofstream   fout;
    std::string     of_name( OUTPUT_FILE_NAME ); 
    fout.open( of_name );

    int num_of_points = atoi(argv[1]);
    int c_pt = atoi(argv[2]);
    float sigma2 = atof(argv[3]);
    float sigma = sqrtf(sigma2);
    std::cout << "Number of points: " << num_of_points          << std::endl;
    std::cout << "C_pt: " << +c_pt                              << std::endl;
    std::cout << "sigma2(variance): " << sigma2                 << std::endl;
    std::cout << "sigma(standard deviation): " << sigma << "\n" << std::endl;

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
    // std::vector<kvs::Vector3d>  plane_points;
    // kvs::Vector3d               plane_point;
    double x, y, z; x = y = z = 0.0;
    int r_noised, g_noised, b_noised; r_noised = g_noised = b_noised = c_pt;

    // Add Gaussian noise to "color" of all 3D points.
    for ( int i = 0 ; i < num_of_points; i++ ) {
        x = uniRand(); // random number [0...1] for x
        y = uniRand(); // random number [0...1] for y
        z = 0.0;

        // Add Gaussian noise
        // if ( i < num_of_points*0.1 ) {
            r_noised = g_noised = b_noised = gaussRand.rand(c_pt, sigma);
            if ( i <= 20 ) {
                std::cout << "(R,G,B) = (" << r_noised << "," << g_noised << "," << b_noised << ")" << std::endl;
            }

            if (r_noised < 0)    r_noised = 0;
            if (r_noised > 255)  r_noised = 255;
            if (g_noised < 0)    g_noised = 0;
            if (g_noised > 255)  g_noised = 255;
            if (b_noised < 0)    b_noised = 0;
            if (b_noised > 255)  b_noised = 255;
                
            // Noise point
            fout << x        << " " << y        << " " << z         << " ";
            fout << 0        << " " << 0        << " " << 0         << " ";
            fout << r_noised << " " << g_noised << " " << b_noised  << "\n";

        // } else {
        //     // Non-noise point
        //     fout << x   << " " << y     << " " << z     << " ";
        //     fout << 0   << " " << 0     << " " << 0     << " ";
        //     fout << 255 << " " << 255   << " " << 255   << "\n";
        // } // end if

        // Show progress
        if ( (i+1) % int(num_of_points*0.1) == 0 ) {
            std::cout << (i*100)/num_of_points+1 << "\% done." << std::endl;
        }
    } // end for

    // FILE close
    fout.close();

    return 0;
}