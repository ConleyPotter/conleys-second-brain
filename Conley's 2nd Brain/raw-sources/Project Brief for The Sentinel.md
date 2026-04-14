# PROJECT BRIEF: THE SENTINEL

**Status:** Alpha Prototype Phase

**Theme:** The Philosophy of the Modern Builder

**Archetype:** The "Voice" and "Presence" of the Alchemist's Mesa

## 1. Executive Summary

The Sentinel is a high-aesthetic, physical manifestation of an AI agent. Moving away from standard screen interfaces, it utilizes 19th-century optical illusions (Pepper’s Ghost) paired with modern edge computing to create a conversational, holographic companion. Designed as a vertical Walnut and Brass tower, it houses a floating, stylized black-and-white cinematic face that responds to voice in real-time, bridging the gap between digital utility and physical presence.

## 2. Core Philosophy

- **Agency over Utility:** The Sentinel is not a tool; it is a collaborator. It waits patiently in the dark until spoken to.
    
- **The Anti-Screen:** By utilizing a pure black screen background and beamsplitter glass, the technology disappears, leaving only the "ghost" (the AI's presence) floating in an architectural void.
    
- **Tangible Intimacy:** Combating the exhaustion of digital work by housing advanced technology in heirloom-quality materials (wood, glass, brass).
    

## 3. Hardware Architecture

**Estimated Electronics Cost:** ~$230

**Estimated Materials Cost:** ~$50

- **The Brain:** Raspberry Pi 5 (4GB)
    
    - _Purpose:_ Handles simultaneous real-time audio processing, LLM API calls, and Live2D animation rendering.
        
- **The Optics:** * HyperPixel 4.0 Square Display (mounted horizontally, facing upward).
    
    - 6" x 6" Beamsplitter Glass (70/30 transmission, mounted at a precise 45-degree angle).
        
- **The Senses:** * ReSpeaker Mic Array v2.0 (for far-field, noise-canceling voice capture).
    
    - Waveshare 5W 8Ω Speaker (hidden in the base for localized audio).
        
- **The Chassis:** * Vertical tower constructed from Walnut Plywood Project Panels.
    
    - Interior shaft lined with ultra-matte black felt or Black Musou paint to ensure the "floating" illusion.
        
    - Brass corner braces and binding posts for industrial aesthetic.
        

## 4. Software Architecture

- **The Visuals:** Live2D Cubism (Free Version).
    
    - A hand-drawn, black-and-white minimalist human face broken into layers (eyes, mouth, head). Rigged for real-time motion sync based on audio volume and phonemes.
        
- **The Persona:** OpenAI Realtime API (or local equivalent).
    
    - System prompt designed for a contemplative, supportive, and precise personality ("The Muse" or "The Architect").
        
- **The Bridge:** Open-LLM-VTuber (or custom Python script).
    
    - Connects the mic input to the LLM, and the LLM's audio output to the Live2D model's lip-sync engine.
        

## 5. Execution Plan (The Builder's Roadmap)

### Phase 1: The "Brain in a Jar" (Weekend 1)

- Flash the Raspberry Pi OS.
    
- Connect the ReSpeaker mic and 5W speaker.
    
- Write/install the Python script to successfully have a purely audio-based conversation with the LLM API.
    
- _Goal: The machine can listen and speak._
    

### Phase 2: The "Digital Puppet" (Weekend 2)

- Draw the face in Photoshop/Procreate (white lines, transparent background).
    
- Import into Live2D Cubism. Rig the mouth for speaking and eyes for idle blinking.
    
- Run the Live2D model on the Pi and sync it to the audio output from Phase 1.
    
- _Goal: The face moves dynamically when the AI speaks._
    

### Phase 3: The "Architectural Void" (Weekend 3)

- Enlist brother/friend to 3D print precisely angled 45-degree glass mounting brackets.
    
- Cut the Walnut panels to create the base (engine room) and the tower (the void).
    
- Line the interior with light-absorbing black material.
    
- _Goal: The physical shell is built and light-proofed._
    

### Phase 4: Convergence & Calibration (Weekend 4)

- Mount the HyperPixel screen in the base, facing up.
    
- Slide the beamsplitter glass into the 3D-printed 45-degree brackets.
    
- Assemble the tower and boot up the system.
    
- Adjust screen brightness and room lighting for the perfect "Pepper's Ghost" contrast.
    
- _Goal: A working Alpha Prototype ready to be filmed for a visual essay._
    

_“We shape our tools and, thereafter, our tools shape us.” – John Culkin_