if __name__ == "__main__": 
    import sys
    sys.path.append('RenderMan/Builds/LinuxMakefile/build')


import librenderman as rm

# Audio settings
sampleRate = 44100
bufferSize = 512
fftSize = 512

# Note settings
midiNote = 60
midiVelocity = 127
noteLength = 4.0
renderLength = 5.0

def create_engine(vst_path):
    engine = rm.RenderEngine(sampleRate, bufferSize, fftSize)
    engine.load_plugin(vst_path)

    return engine

def render_random(engine, override=True):


    # Get a random patch and set it.
    generator = rm.PatchGenerator(engine)
    patch = generator.get_random_patch()
    engine.set_patch(patch)

    if override:
        # We need to override some parameters to prevent hanging notes in
        # Dexed. 
        overriden_parameters = [(26, 1.),  (30, 0.),  (48, 1.),  (52, 0.), 
                                (70, 1.),  (74, 0.),  (92, 1.),  (96, 0.), 
                                (114, 1.), (118, 0.), (136, 1.), (140, 0.)]

        # Loop through each tuple, unpack it and override the correct
        # parameter with the correct value to prevent hanging notes.
        for parameter in overriden_parameters:
            index, value = parameter
            engine.override_plugin_parameter(index, value)

    # Render the data. 
    engine.render_patch(midiNote, midiVelocity, noteLength, renderLength)

    # Get the data. Note the audio is automatically made mono, no
    # matter what channel size for ease of use.
    audio = engine.get_audio_frames()


    return audio, patch

def render_patch(patch_data, engine, override=True):

    

    # Make parameters readable by VST
    patch = [(i,patch_data[i]) for i in range(len(patch_data))]

    # Filling missing parameters with zeros
    while patch[-1][0] < 154:
        patch += [(patch[-1][0]+1,0.)]

    engine.set_patch(patch)

    if override:
        # We need to override some parameters to prevent hanging notes in
        # Dexed. 
        overriden_parameters = [(26, 1.),  (30, 0.),  (48, 1.),  (52, 0.), 
                                (70, 1.),  (74, 0.),  (92, 1.),  (96, 0.), 
                                (114, 1.), (118, 0.), (136, 1.), (140, 0.)]

        # Loop through each tuple, unpack it and override the correct
        # parameter with the correct value to prevent hanging notes.
        for parameter in overriden_parameters:
            index, value = parameter
            engine.override_plugin_parameter(index, value)

    # Render the data. 
    engine.render_patch(midiNote, midiVelocity, noteLength, renderLength)

    # Get the data. Note the audio is automatically made mono, no
    # matter what channel size for ease of use.
    audio = engine.get_audio_frames()

    return audio



if __name__ == "__main__": 
    engine = create_engine("Dexed.so")
    audio, random_patch = render_random(engine)

    # Make parameters readable by VST
    patch = [(i,patch_data[i]) for i in range(len(patch_data))]

    # Filling missing parameters with zeros
    while patch[-1][0] < 154:
        patch += [(patch[-1][0]+1,0.)]



    print("yo")
    print(patch)

