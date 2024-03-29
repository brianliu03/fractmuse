//
//  ContentView.swift
//  FractMuse
//
//  Created by Brian Liu on 10/1/23.
//

import SwiftUI

struct ContentView: View {
    
    var body: some View {
        VStack {
            NavBar()
            Spacer()
            TabBar()
        }
    }
}

struct NavBar: View {

    var body: some View {
        NavigationStack {
            NavigationLink("Text") {
                
            }
        }
    }
}

struct TabBar: View {
    
    var body: some View {
        TabView {
            LibraryView()
                .tabItem { Label("Library", systemImage: "music.note.list") }
            CreateView()
                .tabItem { Label("Create", systemImage: "plus.app.fill") }
            TemplatesView()
                .tabItem { Label("Account", systemImage: "music.quarternote.3") }
        }
    }
}

struct LibraryView: View {
    var body: some View {
        Text("Library")
    }
}

struct CreateView: View {
    var body: some View {
        Text("CreateView")
    }
}

struct TemplatesView: View {
    var body: some View {
        Text("Templates")
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}

#Preview {
    ContentView()
}
