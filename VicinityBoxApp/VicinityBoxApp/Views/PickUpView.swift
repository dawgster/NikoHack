//
//  PickUpView.swift
//  VicinityBoxApp
//
//  Created by Nils Brand on 07.12.19.
//  Copyright © 2019 hypeTech. All rights reserved.
//

//  ListCrudOperationsLBTA
//
//  Created by Brian Voong on 9/23/19.
//  Copyright © 2019 Brian Voong. All rights reserved.

import SwiftUI

import UIKit


struct Person: Identifiable {
    let id = UUID()
    let firstName: String
    let lastName: String
    let image: UIImage
    let jobTitle: String
}

struct PickUpView: View {
    
    @State var latest: [Person] = [
        .init(firstName: "Helge",
              lastName: "Zurbrüggen", image: #imageLiteral(resourceName: "HZ"), jobTitle: "Digital Devotion Group")
    ]
    
//@State var people: [Person] = [
    @State var history: [Person] = [
        .init(firstName: "DHL",
              lastName: "", image: #imageLiteral(resourceName: "dhl-logo"), jobTitle: "Parcel Service"),
        .init(firstName: "Chantal", lastName: "Momber", image: #imageLiteral(resourceName: "CM"), jobTitle: "OD Pfalz"),
        .init(firstName: "Hermes", lastName: "", image: #imageLiteral(resourceName: "hermes"), jobTitle: "Parcel Service"),
        .init(firstName: "Jonas", lastName: "Rupp", image: #imageLiteral(resourceName: "JR"), jobTitle: "Vice President KaRaT"),
           .init(firstName: "Christoph", lastName: "Grimm", image: #imageLiteral(resourceName: "CG"), jobTitle: "Chair Owner CPS")
    ]
    
    var body: some View {
        VStack{
        NavigationView{
        
            List(latest) { person in
                PersonRow(person: person, didDelete: { p in
                    self.latest.removeAll(where: {$0.id == person.id})
                })
            }.navigationBarTitle("Latest")
        }
        
        
        
        NavigationView {
            
            List(history) { person in
                PersonRow(person: person, didDelete: { p in
                    self.history.removeAll(where: {$0.id == person.id})
                })
            }.navigationBarTitle("History")
        }
    }
    }
}

struct PersonRow: View {
    
    var person: Person
    var didDelete: (Person) -> ()
    
    var body: some View {
        HStack {
            Image(uiImage: person.image)
                .resizable()
                .scaledToFill()
                .frame(width: 60, height: 60)
                .overlay(
                    RoundedRectangle(cornerRadius: 60)
                        .strokeBorder(style: StrokeStyle(lineWidth: 2))
                        .foregroundColor(Color.black))
                .cornerRadius(60)
            
            VStack (alignment: .leading) {
                Text("\(person.firstName) \(person.lastName)")
                    .fontWeight(.bold)
                Text(person.jobTitle)
                    .fontWeight(.light)
            }.layoutPriority(1)
            
            Spacer()
            /*
            Button(action: {
                self.didDelete(self.person)
            }, label: {
                Text("Delete")
                    .foregroundColor(.white)
                    .fontWeight(.bold)
                    .padding(.all, 12)
                    .background(Color.red)
                    .cornerRadius(3)
            })*/
            
        }.padding(.vertical, 8) //padding(.vertical, 8)
    }
}
/*
struct PickUpView: View {
    var body: some View {
        
        VStack {
            Text("Pickup").font(.headline)
        
        HStack {
            Spacer()
            Image("profile-pic")
                       .resizable()
                       .frame(width: 50, height: 50)
                   Text("Daniel left something for you")
                   Spacer()
               }
        }
    }
}*/

struct PickUpView_Previews: PreviewProvider {
    static var previews: some View {
        PickUpView()
    }
}
