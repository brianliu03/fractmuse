//
//  ContentView.swift
//  FractMuse
//
//  Created by Brian Liu on 9/15/23.
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
            
        }
//        VStack(spacing: 0) {
//            VStack(alignment: .leading, spacing: 0) {
//                HStack(spacing: 0) {
//                    HStack(spacing: 16) {
//                        HStack(alignment: .top, spacing: 10) {
//                            Text("􀈙")
//                                .font(Font.custom("SF Pro", size: 17))
//                                .lineSpacing(22)
//                                .foregroundColor(Color(red: 0, green: 0.48, blue: 1))
//                        }
//                    }
//                    .padding(EdgeInsets(top: 11, leading: 0, bottom: 11, trailing: 16))
//                }
//                .padding(EdgeInsets(top: 0, leading: 347, bottom: 0, trailing: 0))
//                .frame(width: 393)
//                VStack(alignment: .leading, spacing: 10) {
//                    Text("Compositions")
//                        .font(Font.custom("SF Pro", size: 34).weight(.bold))
//                        .lineSpacing(41)
//                        .foregroundColor(.black)
//                }
//                .padding(EdgeInsets(top: 3, leading: 16, bottom: 8, trailing: 16))
//                .frame(maxWidth: .infinity, minHeight: 52, maxHeight: 52)
//            }
//            .frame(maxWidth: .infinity, minHeight: 96, maxHeight: 96)
//        }
//        .frame(width: 393, height: 150)
//        .background(Color(red: 1, green: 1, blue: 1).opacity(0.75))
//        .overlay(
//            Rectangle()
//                .inset(by: 0.17)
//                .stroke(
//                    Color(red: 0, green: 0, blue: 0).opacity(0.30), lineWidth: 0.17
//                )
//        )
    }
}

struct TabBar: View {
    
    var body: some View {
        TabView {
            LibraryView()
                .badge(2)
                .tabItem { Label("Library", systemImage: "music.note.list") }
            CreateView()
                .tabItem { Label("Create", systemImage: "plus.app.fill") }
            TemplatesView()
                .badge("!")
                .tabItem { Label("Account", systemImage: "music.quarternote.3") }
        }
    }
}

struct LibraryView: View {
    var body: some View {
        VStack(alignment: .center, spacing: 7) {
            Image(systemName: "music.note.list")
              .font(
                Font.custom("SF Pro", size: 18)
                  .weight(.medium)
              )
            Text("Library")
              .font(
                Font.custom("SF Pro", size: 10)
                  .weight(.medium)
              )
              .multilineTextAlignment(.center)
        }
        .multilineTextAlignment(.center)
        .foregroundColor(Color(red: 0.6, green: 0.6, blue: 0.6))
        .padding(.horizontal, 6.5)
        .padding(.vertical, 0)
        .frame(width: 48, height: 40, alignment: .center)
    }
}

struct CreateView: View {
    var body: some View {
        VStack(alignment: .center, spacing: 7) {
            Image(systemName: "music.note.list")
              .font(
                Font.custom("SF Pro", size: 18)
                  .weight(.medium)
              )
            Text("Library")
              .font(
                Font.custom("SF Pro", size: 10)
                  .weight(.medium)
              )
              .multilineTextAlignment(.center)
        }
        .multilineTextAlignment(.center)
        .foregroundColor(Color(red: 0.6, green: 0.6, blue: 0.6))
        .padding(.horizontal, 6.5)
        .padding(.vertical, 0)
        .frame(width: 48, height: 40, alignment: .center)
    }
}

struct TemplatesView: View {
    var body: some View {
        VStack(alignment: .center, spacing: 7) {
            Image(systemName: "music.note.list")
              .font(
                Font.custom("SF Pro", size: 18)
                  .weight(.medium)
              )
            Text("Library")
              .font(
                Font.custom("SF Pro", size: 10)
                  .weight(.medium)
              )
              .multilineTextAlignment(.center)
        }
        .multilineTextAlignment(.center)
        .foregroundColor(Color(red: 0.6, green: 0.6, blue: 0.6))
        .padding(.horizontal, 6.5)
        .padding(.vertical, 0)
        .frame(width: 48, height: 40, alignment: .center)
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
