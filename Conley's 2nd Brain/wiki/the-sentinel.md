# The Sentinel

**Tags:** project, hardware, vision, aspiration  
**Sources:** Project Brief for The Sentinel.md, Personal Portfolio Website Current State 4.14.26.md  
**Related:** [[ace-overview]], [[conley-potter]], [[portfolio-website]]

---

## Status and Nature

**Status:** Alpha Prototype Phase — aspirational / in planning

The Sentinel is not an active build. It is a vision Conley is working toward, contingent on ACE generating the revenue and seed capital to fund it. This is the directional north star, not the current priority. See [[ace-overview]] — "ACE as Seed Capital for The Sentinel."

The portfolio website lists it as "In Development," which is an aspirational framing. The project brief exists, the design is fully conceived, and the hardware BOM is priced out. It has not been built yet.

---

## Executive Summary

> "A high-aesthetic, physical manifestation of an AI agent. Moving away from standard screen interfaces, it utilizes 19th-century optical illusions (Pepper's Ghost) paired with modern edge computing to create a conversational, holographic companion. Designed as a vertical Walnut and Brass tower, it houses a floating, stylized black-and-white cinematic face that responds to voice in real-time, bridging the gap between digital utility and physical presence."

The Sentinel is the antithesis of a laptop or a phone. It exists as a physical object in the room, with weight and materials and a face that appears to float in mid-air. It talks back.

---

## Core Philosophy

Three design principles define everything about The Sentinel:

**Agency over Utility.** The Sentinel is not a tool — it is a collaborator. It waits patiently in the dark until spoken to. The distinction matters: tools are picked up and put down; collaborators have presence.

**The Anti-Screen.** By using a pure black background and beamsplitter glass, the technology disappears. What's left is a "ghost" — the AI's presence — floating in an architectural void. No bezel, no UI chrome, no screen. Just the face.

**Tangible Intimacy.** Walnut plywood and brass hardware are not aesthetic choices for the sake of aesthetics. They are a deliberate counter to the exhaustion of digital work — heirloom-quality materials that make something lasting out of something usually disposable.

The theme Conley associates with this: **"The Philosophy of the Modern Builder."** The archetype: **"The Voice and Presence of the Alchemist's Mesa."**

---

## Hardware Architecture

**Estimated total cost: ~$280** ($230 electronics + $50 materials)

| Component | Part | Purpose |
|---|---|---|
| **The Brain** | Raspberry Pi 5 (4GB) | Handles simultaneous real-time audio processing, LLM API calls, and Live2D animation rendering |
| **The Display** | HyperPixel 4.0 Square Display | Mounted horizontally, facing upward into the beamsplitter |
| **The Optics** | 6" × 6" Beamsplitter Glass (70/30 transmission) | Mounted at precise 45° angle — creates the Pepper's Ghost floating face illusion |
| **The Ears** | ReSpeaker Mic Array v2.0 | Far-field, noise-canceling voice capture |
| **The Voice** | Waveshare 5W 8Ω Speaker | Hidden in the base for localized audio |
| **The Shell** | Walnut Plywood Project Panels | Vertical tower: base ("engine room") + tower ("the void") |
| **The Void** | Ultra-matte black felt or Black Musou paint | Interior lining — ensures light absorption, maximizes floating illusion |
| **The Detail** | Brass corner braces and binding posts | Industrial aesthetic, structural |

### How Pepper's Ghost Works Here

The HyperPixel display sits in the base, facing upward. The beamsplitter glass sits above it at a 45° angle. The display renders the face against a pure black background. The glass reflects the image upward at 45°, so the face appears to float in the middle of the tower's dark void. The glass is also partially transparent — you can see through it to the void behind — which makes the face look like it's hovering in empty space rather than projected on a surface.

---

## Software Architecture

| Layer           | Technology                                | Role                                                                                                                                        |
| --------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **The Visuals** | Live2D Cubism (Free Version)              | A hand-drawn, black-and-white minimalist human face, rigged for real-time motion sync — mouth and eyes respond to audio volume and phonemes |
| **The Persona** | OpenAI Realtime API (or local equivalent) | Contemplative, supportive, precise personality — system prompt defines "The Muse" or "The Architect" character                              |
| **The Bridge**  | Open-LLM-VTuber or custom Python script   | Connects mic input → LLM → audio output → Live2D lip-sync engine                                                                            |

---

## Execution Plan (Four Weekends)

### Phase 1: Brain in a Jar (Weekend 1)
- Flash Raspberry Pi OS
- Connect ReSpeaker mic and speaker
- Python script: audio-based conversation with LLM API
- **Goal:** The machine can listen and speak

### Phase 2: The Digital Puppet (Weekend 2)
- Draw the face in Photoshop/Procreate (white lines, transparent background)
- Import into Live2D Cubism; rig mouth for speaking, eyes for idle blinking
- Run Live2D on the Pi; sync to audio output from Phase 1
- **Goal:** The face moves dynamically when the AI speaks

### Phase 3: The Architectural Void (Weekend 3)
- Enlist someone to 3D-print precisely angled 45° glass mounting brackets
- Cut Walnut panels for base (engine room) and tower (the void)
- Line interior with light-absorbing black material
- **Goal:** Physical shell built and light-proofed

### Phase 4: Convergence & Calibration (Weekend 4)
- Mount HyperPixel screen in the base, facing up
- Slide beamsplitter into 3D-printed brackets
- Assemble tower, boot system
- Adjust brightness and room lighting for perfect Pepper's Ghost contrast
- **Goal:** Working Alpha Prototype, ready to be filmed for a visual essay

---

## Relationship to ACE

The Sentinel and ACE are connected through a funding dependency, not a technical one:

- ACE is the revenue engine — freelance arbitrage generating operating capital and runway
- The Sentinel is the destination — what that capital eventually funds
- ACE Phase I (B2B lead enrichment) → operating revenue → personal stability + seed capital → The Sentinel build

The Sentinel also represents a different mode of thinking than ACE. ACE is pragmatic, commercially oriented, optimized for margin. The Sentinel is philosophical — it's about what it means to build physical things with care, to give AI a body, to make technology feel intimate rather than exhausting. They are the same builder at different registers.

---

## Output Intent

The Alpha Prototype is explicitly designed to be filmed for **a visual essay** — not just a working prototype for personal use, but a piece of content that documents the build and the philosophy behind it. This connects to the Thought Leader Engine and Conley's broader building-in-public strategy on Threads.

> *"We shape our tools and, thereafter, our tools shape us." — John Culkin*
