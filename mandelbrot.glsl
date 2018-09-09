// Displays the Mandelbrot set. Run on Shadertoy.com.
#define R iResolution.xy
void mainImage( out vec4 O, in vec2 I ) {
    vec2 c = ( 2.*I - R ) / R.y, z = 0./R; 
    float i = 0.;
	for(; ++i <= 64. && dot(z,z) < 4. ;)
        z = mat2( z, -z.y, z.x ) * z + c;
    O = vec4(vec3( i / 64. ), 1.0);
}