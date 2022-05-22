import javax.sound.midi.*;
import java.util.List;

public class MidiInterface {

    public MidiInterface() {
        MidiDevice device;
        MidiDevice.Info[] infos = MidiSystem.getMidiDeviceInfo();
        for (int i = 0; i < infos.length; i++) {
            try {
            device = MidiSystem.getMidiDevice(infos[i]);
            //does the device have any transmitters?
            //if it does, add it to the device list
            System.out.println(infos[i]);

            //get all transmitters
            List<Transmitter> transmitters = device.getTransmitters();
            //and for each transmitter
            

            for(int j = 0; j<transmitters.size();j++) {
                //create a new receiver
                transmitters.get(j).setReceiver(
                        //using my own MidiInputReceiver
                        new MidiInputReceiver(device.getDeviceInfo().toString())
                );
            }

            Transmitter trans = device.getTransmitter();
            trans.setReceiver(new MidiInputReceiver(device.getDeviceInfo().toString()));

            //open each device
            device.open();
            //if code gets this far without throwing an exception
            //print a success message
            System.out.println(device.getDeviceInfo()+" Was Opened");

            Sequencer sequencer = MidiSystem.getSequencer();
            sequencer.open();


        } catch (MidiUnavailableException e) {}
    }
}


// tried to write my own class. I thought the send method handles an MidiEvents sent to it
public class MidiInputReceiver implements Receiver {
    public String name;
    public MidiInputReceiver(String name) {
        this.name = name;
    }
    public void send(MidiMessage msg, long timeStamp) {
        System.out.println("midi received");
    }
    public void close() {}
    }
}