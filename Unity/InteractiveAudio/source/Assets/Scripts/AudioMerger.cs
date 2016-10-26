using UnityEngine;
using System.Collections;

public class AudioMerger : MonoBehaviour
{
    public AudioClip[] channels;
    public AudioClip channelsMix;
 

    void Awake()
    {
       
    }

	// Use this for initialization
	void Start()
	{
        channelsMix = AudioClip.Create("Mixed tracks", channels[0].samples, channels[0].channels, channels[0].frequency, false);
        float[] tmp = new float[channels[0].samples * channels[0].channels];
        channelsMix.SetData(tmp, 0);

        foreach (AudioClip channel in channels)
        {
            float[] mixedChannelSamples = new float[channelsMix.samples * channelsMix.channels];
            channelsMix.GetData(mixedChannelSamples, 0);

            float[] currentChannelSamples = new float[channel.samples * channel.channels];
            channel.GetData(currentChannelSamples, 0);

            float[] temp = new float[mixedChannelSamples.Length];
            temp = mixLinearTracks(ref mixedChannelSamples, ref currentChannelSamples);

            channelsMix.SetData(temp, 0);
        }

        Debug.Log("Done !");

        AudioSource _audioSource = GetComponent<AudioSource>();
        _audioSource.clip = channelsMix;
        _audioSource.Play();

        Debug.Log("Play !");



        
	}
	
	// Update is called once per frame
	void Update()
	{
	    
	}
    
    /*
    public AudioClip mixAudioClips(AudioClip audioClipA, AudioClip audioClipB)
    {
        float[] samplesA = new float[audioClipA.samples * audioClipA.channels];
        audioClipA.GetData(samplesA, 0);

        float[] samplesB = new float[audioClipB.samples * audioClipB.channels];
        audioClipB.GetData(samplesB, 0);

        float[] mixedSamples = mixTracks(ref samplesA, ref samplesB);

        AudioClip temp = AudioClip.Create("Mixed track", mixedSamples.Length / 2, audioClipA.channels, audioClipA.frequency, false);
        temp.SetData(mixedSamples, 0);

        return temp;
    }

    */

    // Fusionne deux tableaux de samples (flottants) de même longueur
    // en un seul tableau en utilisant l'algorithme de fusion de deux morceaux
    public float[] mixLinearTracks(ref float[] trackA, ref float[] trackB)
    {
        int minLength = trackA.Length > trackB.Length ? trackB.Length : trackA.Length;

        float[] mixedTrack = new float[minLength];

        for (int i = 0; i < mixedTrack.Length; i++)
            mixedTrack[i] = mixSamples(trackA[i], trackB[i]);

        return mixedTrack;
    }

    // Mélange deux samples selon un algorithme utile pour fusionner deux morceaux
    public float mixSamples(float sampleA, float sampleB)
    {
        if (sampleA < 0f && sampleB < 0f)
        {              
            return sampleA + sampleB + sampleA*sampleB;
            //return (sampleA + sampleB) - ((sampleA * sampleB) / -1f);
        }
        else if (sampleA > 0f && sampleB > 0f)
        {
            return sampleA + sampleB - sampleA*sampleB;
        }
        else
        {
            return sampleA + sampleB;
        }
    }
}
