//
//  ContentView.swift
//  FractMuse
//
//  Created by Brian Liu on 9/15/23.
//

import SwiftUI

struct ContentView: View {
    
    var body: some View {
//        NavBar()
        TabBar()
    }
}

//struct NavBar: View {
//    var body: some View {
//
//    }
//}

struct TabBar: View {
    var body: some View {
        HStack(alignment: .top) {
            // Space Between
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
            Spacer()
            // Alternative Views and Spacers
            VStack(alignment: .center, spacing: 7) {
                Image(systemName: "plus.square.fill")
                  .font(
                    Font.custom("SF Pro", size: 18)
                      .weight(.medium)
                  )
                  .multilineTextAlignment(.center)
                  .foregroundColor(Color(red: 0.6, green: 0.6, blue: 0.6))
                Text("Create")
                  .font(
                    Font.custom("SF Pro", size: 10)
                      .weight(.medium)
                  )
                  .multilineTextAlignment(.center)
                  .foregroundColor(Color(red: 0.6, green: 0.6, blue: 0.6))
            }
            .padding(.horizontal, 7.5)
            .padding(.vertical, 0)
            .frame(width: 48, height: 40, alignment: .center)
            Spacer()
            VStack(alignment: .center, spacing: 7) {
                Image(systemName: "music.quarternote.3")
                  .font(
                    Font.custom("SF Pro", size: 18)
                      .weight(.medium)
                  )
                  .multilineTextAlignment(.center)
                  .foregroundColor(Color(red: 0.6, green: 0.6, blue: 0.6))
                Text("Templates")
                  .font(
                    Font.custom("SF Pro", size: 10)
                      .weight(.medium)
                  )
                  .multilineTextAlignment(.center)
                  .foregroundColor(Color(red: 0.6, green: 0.6, blue: 0.6))
            }
            .padding(0)
            .frame(width: 48, height: 40, alignment: .center)
            
        }
        .padding(.horizontal, 15)
        .padding(.vertical, 0)
        .frame(width: 394, alignment: .top)
        .padding(.horizontal, 0)
        .padding(.top, 7)
        .padding(.bottom, 36)
        .frame(width: 393, height: 83, alignment: .center)
        .background(.white.opacity(0.75))
        .shadow(color: .black.opacity(0.3), radius: 0, x: 0, y: -0.33)
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
