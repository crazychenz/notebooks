## Rust On Windows for Godot

Vaguely following advice from:

https://medium.com/@recallsingularity/gorgeous-godot-games-in-rust-1867c56045e6

1. Install Visual Studio **C++ Build Tools** 2019, not Visual Studio 2019. https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019

   I attempted to have everything install into my D:\ drive, and yet Microsoft insisted on installing ~2.1  GB to my C:\ drive. (Strike #1 for this crap environment setup.) *I've already called ahead for the reservation in hell for the prick who made that design decision.* Silver lining is that I was able to stick at least 3GB of the install onto a non-system drive.

2. Install rust by going to https://www.rust-lang.org/tools/install and implicitly/explicitly run the downloaded content.

   For simplicity, I'm adding the resulting EXE to my newly created C:\bin directory.

   **BUG**: I would have prefered to set CARGO_HOME to D:\rust\cargo and RUSTUP_HOME to D:\rust\rustup, but there is apparently a bug preventing this from happening and I am refusing to get sucked down that rabbit hole for now. (Strike #2 for this crap environment setup.) Forced to go with the default setup of %HOME%/.cargo and %HOME%/.rustup for now. 

3. ~~Install LLVM by going to https://releases.llvm.org/download.html and running the downloaded content. (*Finally an installer that has been developed with some respect for the user!*)~~
   You can't just install LLVM for windows because the pre-built binaries don't include llvm-config for some very unknown reason. To build LLVM from source code:

   1. Install CMAKE (3.5 or newer) https://cmake.org/download/.
   2. 

4. Clone godot-rust bindings from https://github.com/GodotNativeTools/godot-rust.git

5. Run `cargo build` from PATH/godot-rust/examples/hello_world

6. sdf

7. sdf

8. sdf

9. 