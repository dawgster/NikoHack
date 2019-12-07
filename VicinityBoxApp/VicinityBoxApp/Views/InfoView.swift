//
//  InfoView.swift
//  VicinityBoxApp
//
//  Created by Nils Brand on 07.12.19.
//  Copyright © 2019 hypeTech. All rights reserved.
//
//
//  ContentView.swift
//  ListCrudOperationsLBTA
//
//  Created by Brian Voong on 9/23/19.
//  Copyright © 2019 Brian Voong. All rights reserved.
//

import SwiftUI


struct InfoView: View {
    let love = Image(systemName: "heart.fill")
    var body: some View {
        HStack{
        Text("Made with")
            Image(systemName: "heart.fill").foregroundColor(Color.red)
        Text("in Kaiserslautern")
        }
    }
}

struct InfoView_Previews: PreviewProvider {
    static var previews: some View {
        InfoView()
    }
}
