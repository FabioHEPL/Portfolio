using UnityEngine;
using System.Collections;

public class LightAnimation : MonoBehaviour
{
    private AudioSource _audioSource = null;
    private AudioClip animatorClip = null;

    public float scaling = 20f;

    private float[] signalAmplitude = new float[512];

    public float tresholdAmplitude = 0.2f;

    Vector3 startPosition;

    private Vector3 translateVelocity = Vector3.zero;
    private Vector3 resetVelocity = Vector3.zero;
    public float smoothing = 0.1f;

    public bool smoothMovement = true;

    public Light lighto;


    // Use this for initialization
    void Start()
    {
        startPosition = transform.position;
    
        _audioSource = GetComponent<AudioSource>();
        animatorClip = _audioSource.clip;
    }

    // Update is called once per frame
    void Update()
    {
        _audioSource.GetOutputData(signalAmplitude, 0);
        float amplitude = calculateAmplitude(signalAmplitude);

     
    }

    public float calculateAmplitude(float[] samples)
    {
        float samplesSum = 0f;

        for (int i = 0; i < samples.Length; i++)
        {
            samplesSum += samples[i] * samples[i];
        }

        return (float)System.Math.Sqrt(samplesSum / samples.Length);
    }
}
