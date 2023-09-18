//
//  ContentView.swift
//  FractMuse
//
//  Created by Brian Liu on 9/15/23.
//

import SwiftUI

struct ContentView: View {
    
    var body: some View {
        HStack {
            VStack {
                Text("Compositions")
                Button("New") {
                    print("pressed")
                }
            }
            Text("Content")
        }
        .padding()
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
