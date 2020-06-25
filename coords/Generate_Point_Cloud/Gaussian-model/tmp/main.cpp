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

const char OUTPUT_NOISED_SPBR[] = "SPBR_DATA/plane_coords_noise.spbr";

int main(int argc, char **argv) {
    if ( argc != 4 ) {
        std::cout << "USAGE  : " << argv[0] << " [num. of points] [sigma2(variance)] [ratio_for_adding_noise]" << std::endl;
        std::cout << "EXAMPLE: " << argv[0] << "1000000 0.01 0.1" << std::endl;
        exit(1);
    }

    // FILE open
    std::ofstream   fout;
    std::string     of_name( OUTPUT_NOISED_SPBR ); 
    fout.open( of_name );

    int num_of_points = atoi(argv[1]);
    float sigma2 = atof(argv[2]);
    std::cout << "Number of points: " << num_of_points << std::endl;
    std::cout << "Sigma2(Variance): " << sigma2     << std::endl;
    std::cout << "Sigma: " << sqrtf(sigma2)         << std::endl;

    // variables
    kvs::MersenneTwister        uniRand;
    std::vector<kvs::Vector3d>  plane_points;
    kvs::Vector3d               plane_point;
    double x, y, z; x = y = z = 0.0;
    kvs::BoxMuller  gaussRand;
    kvs::Vector3d   point;
    float ratio_for_add_noise = atof(argv[3]);
    int noise_counter = 0;

    // Set SPBR header
    fout << "#/SPBR_ASCII_Data"      << std::endl;
    fout << "#/RepeatLevel 1"        << std::endl;
    fout << "#/BGColorRGBByte 0 0 0" << std::endl;
    fout << "#/ImageResolution 512"  << std::endl;
    fout << "#/Shading 0"            << std::endl;
    fout << "#/LOD 0"                << std::endl;
    fout << "#/EndHeader"            << std::endl;

    // Stochastically, add noise to point cloud
    std::cout << "Adding noise... (with " << ratio_for_add_noise*100 << "%)\n" << std::endl;

    // Generate the point cloud
    for ( int i = 0 ; i < num_of_points; i++ ) {
        x = uniRand(); // random number [0...1] for x
        y = uniRand(); // random number [0...1] for y
        z = 0.0;

        // Noise point (Red)
        if ( i < num_of_points*ratio_for_add_noise ) {
            // N(μ, σ^2)
            // N(0, 1) → μ=0, σ^2=1

            // Add Gaussian noise
            // x += gaussRand.rand(0, sigma2);
            // y += gaussRand.rand(0, sigma2);
            z += gaussRand.rand(0, sigma2);
            // z = uniRand()*0.02 - 0.01; // Kanda ver.

            // Write to .spbr file 
            fout << x   << " " << y << " " << z << " ";
            fout << 0   << " " << 0 << " " << 0 << " ";
            fout << 255 << " " << 0 << " " << 0 << std::endl; // Red

            // Count number of noised points
            noise_counter++;

        // Not noise point (White)
        } else {
            fout << x   << " " << y   << " " << z   << " ";
            fout << 0   << " " << 0   << " " << 0   << " ";
            fout << 255 << " " << 255 << " " << 255 << std::endl; // White
        } // end if

        // Show progress
        if ( (i+1) % int(num_of_points*0.1) == 0 ) {
            std::cout << (i*100)/num_of_points+1 << "\% done." << std::endl;
        }
    } // end for

    std::cout << "\nNumber of noised points"    << std::endl;
    std::cout << "> " << noise_counter << "\n"  << std::endl;  

    // FILE close
    fout.close();

    return 0;
}