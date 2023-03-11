# hxpCTF 2023
## Pwn
1. hypersecure by sisu

Difficulty estimate: ```medium```

Description: ``` Don’t we all love hypervisors <3 ```

Connection (mirrors): ``` nc 162.55.59.179 8120 ```

2. shadertoy_plus_plus by sisu

Difficulty estimate: ```hard```

Description:

	Want to do some shader programming but GPUs still too expensive? WebGL is fun but Chrome eats all your memory? Graphics APIs still suck?

	At HXP, we offer the best abstractions for your needs: shadertoy compute shaders. Just don’t hack our abstractions.

	For your convenience:

	The challenge relies on a few too many projects, but that’s how software is built.

	    ANGLE for implementing GLES 3.1: https://github.com/google/angle/
	    SwiftShader for a CPU-based Vulkan implementation: https://github.com/google/swiftshader
	    fpng for converting raw image data to PNG: https://github.com/richgel999/fpng
	    a bunch of other libraries which are used for building and supporting ANGLE, swiftshader

	The challenge is specifically targetting ___ ANGLE and SwiftShader ___. If you find a bug somewhere else in our piece of code, please go ahead and exploit it.

	The source files for ‘hxp_gpu’ should not have bugs, but who knows.

	Structure:

	    ’/standalone_build’ This one contains a dockerfile for building the binaries for hosting the challenge. This includes the full ANGLE project and hxp_gpu. The source files for ‘hxp_gpu’ are there. The standalone build will take some time, about 20m-40m on a laptop.

	    ’/example_client’ This provides an example how to communicate with ‘hxp_gpu’. It even provides a compute shader to render an image with high aesthetics!

	    “everything else” This one contains the challenge files without any source code. There should be no reason to reverse the binaries except for what’s necessary for exploitation. The dockerfile inside is for hosting the challenge locally.

## Rev
1. required by sandr0

Difficulty estimate: ```easy```

Description:

	I have written a super safe flag encryptor. I’m sure nobody can figure out what my original flag was:

	0xd19ee193b461fd8d1452e7659acb1f47dc3ed445c8eb4ff191b1abfa7969

	Dockerfile for your convenience / to ensure correct environment.

2. tex_based_adventure by hlt

Difficulty estimate: ```medium```

Description:

	Here’s our yearly “wait, you can actually code in this?” challenge.

3. linear_code by iead

Difficulty estimate: ```hard```

Description:

	linear code

	haunted by soul crushing RE nightmares

	精神をつぶすのRE悪夢に祟られる。

	頑張ってね。

	Special Thanks To: kirschju, Christopher Domas (@xoreaxeaxeax)