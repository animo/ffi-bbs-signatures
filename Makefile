ios-all: prepare headers ios-build ios-lipo ios-xcframework ios-move header-move

clean:
	rm -rf dist/ios/*

headers: 
	./scripts/generate-cpp-header.sh

prepare:
	cargo install cbindgen
	rustup target add aarch64-apple-ios
	rustup target add aarch64-apple-ios-sim
	rustup target add x86_64-apple-ios
	mkdir -p dist/ios/

ios-lipo:
	lipo -create ./target/x86_64-apple-ios/release/libbbs.a  \
		           ./target/aarch64-apple-ios-sim/release/libbbs.a \
			 -output ./dist/ios/libbbs.a

ios-build:
	cargo build --release --target aarch64-apple-ios
	cargo build --release --target aarch64-apple-ios-sim
	cargo build --release --target x86_64-apple-ios

ios-xcframework:
	xcodebuild -create-xcframework \
				 		 -library ./target/aarch64-apple-ios/release/libbbs.a -headers include/bbs.hpp \
				 		 -library ./dist/ios/libbbs.a                         -headers include/bbs.hpp \
				 		 -output  ./dist/ios/BbsSignatures.xcframework

ios-move:
	rm -rf ../react-native-bbs-signatures/ios/Frameworks/BbsSignatures.xcframework
	cp -r ./dist/ios/BbsSignatures.xcframework ../react-native-bbs-signatures/ios/Frameworks/

header-move:
	rm -rf ../react-native-bbs-signatures/cpp/bbs.h
	cp ./include/bbs.hpp ../react-native-bbs-signatures/cpp/bbs.h
