// adapted from the following examples:
// - the video capture example http://processing.org/reference/libraries/video/Capture.html
// - the blob detection example http://www.v3ga.net/processing/BlobDetection/index-page-download.html
// - the video background subtraction example https://github.com/processing/processing/tree/master/java/libraries/video/examples/Capture/BackgroundSubtraction

import processing.video.*;
import blobDetection.*;

Capture cam;
BlobDetection theBlobDetection;
PImage img, bg;
int numPixels;
int[] backgroundPixels;

boolean newFrame=false;
int mode = 0;

// ==================================================
// setup()
// ==================================================
void setup()
{
  // Size of applet
  size(640/2, 480/2);
  // Capture
  cam = new Capture(this, width, height, 30);
  // Comment the following line if you use Processing 1.5
  cam.start();
        
  // BlobDetection
  // img which will be sent to detection (a smaller copy of the cam frame);
  img = new PImage(width,height);
  bg = new PImage(width,height);  
  theBlobDetection = new BlobDetection(img.width, img.height);
  theBlobDetection.setPosDiscrimination(true);
  theBlobDetection.setThreshold(0.2f); // will detect bright areas whose luminosity > 0.2f;
  
  numPixels = cam.width * cam.height;
  // Create array to store the background image
  backgroundPixels = new int[numPixels];
  loadPixels();
}

// ==================================================
// captureEvent()
// ==================================================
void captureEvent(Capture cam)
{
  cam.read();
  newFrame = true;
}

// ==================================================
// draw()
// ==================================================
void draw()
{  
  if (newFrame)
  {
    newFrame=false;
    if(mode == 0)
    { 
      image(bg,0,0,width,height);  
      text("bg image", 20, 20); 
    }
    else if(mode == 1)
    { 
      image(cam,0,0,width,height);  
      text("camera image", 20, 20); 
    }
    else if (mode == 2)
    { 
      // Difference between the current frame and the stored background
    int presenceSum = 0;
    for (int i = 0; i < numPixels; i++) { // For each pixel in the video frame...
      // Fetch the current color in that location, and also the color
      // of the background in that spot
      color currColor = cam.pixels[i];
      color bkgdColor = backgroundPixels[i];
      // Extract the red, green, and blue components of the current pixel�s color
      int currR = (currColor >> 16) & 0xFF;
      int currG = (currColor >> 8) & 0xFF;
      int currB = currColor & 0xFF;
      // Extract the red, green, and blue components of the background pixel�s color
      int bkgdR = (bkgdColor >> 16) & 0xFF;
      int bkgdG = (bkgdColor >> 8) & 0xFF;
      int bkgdB = bkgdColor & 0xFF;
      // Compute the difference of the red, green, and blue values
      int diffR = abs(currR - bkgdR);
      int diffG = abs(currG - bkgdG);
      int diffB = abs(currB - bkgdB);
      // Add these differences to the running tally
      presenceSum += diffR + diffG + diffB;
      // Render the difference image to the screen
      pixels[i] = color(diffR, diffG, diffB);
      // The following line does the same thing much faster, but is more technical
      //pixels[i] = 0xFF000000 | (diffR << 16) | (diffG << 8) | diffB;
    }
    updatePixels(); // Notify that the pixels[] array has changed
    println(presenceSum); // Print out the total amount of movement
    
      text("with bg subtracted", 20, 20); 
    }
    
    img.loadPixels();
    arraycopy(pixels,img.pixels);
    img.updatePixels();
    fastblur(img, 2);
    theBlobDetection.computeBlobs(img.pixels);
    drawBlobsAndEdges(true,true);
  }
}

void keyPressed()
{
  if(key == ' ')
  {
    cam.loadPixels();
    arraycopy(cam.pixels, backgroundPixels);
    bg.copy(cam, 0, 0, cam.width, cam.height, 
                 0, 0, bg.width, bg.height);
  }
  else
  { mode = (mode+1)%3; }
}

// ==================================================
// drawBlobsAndEdges()
// ==================================================
void drawBlobsAndEdges(boolean drawBlobs, boolean drawEdges)
{
  noFill();
  Blob b;
  EdgeVertex eA,eB;
  for (int n=0 ; n<theBlobDetection.getBlobNb() ; n++)
  {
    b=theBlobDetection.getBlob(n);
    if (b!=null)
    {
      // Edges
      if (drawEdges)
      {
        strokeWeight(3);
        stroke(0,255,0);
        for (int m=0;m<b.getEdgeNb();m++)
        {
          eA = b.getEdgeVertexA(m);
          eB = b.getEdgeVertexB(m);
          if (eA !=null && eB !=null)
            line(
              eA.x*width, eA.y*height, 
              eB.x*width, eB.y*height
              );
        }
      }

      // Blobs
      if (drawBlobs)
      {
        strokeWeight(1);
        stroke(255,0,0);
        rect(
          b.xMin*width,b.yMin*height,
          b.w*width,b.h*height
          );
      }

    }

      }
}

// ==================================================
// Super Fast Blur v1.1
// by Mario Klingemann 
// <http://incubator.quasimondo.com>
// ==================================================
void fastblur(PImage img,int radius)
{
 if (radius<1){
    return;
  }
  int w=img.width;
  int h=img.height;
  int wm=w-1;
  int hm=h-1;
  int wh=w*h;
  int div=radius+radius+1;
  int r[]=new int[wh];
  int g[]=new int[wh];
  int b[]=new int[wh];
  int rsum,gsum,bsum,x,y,i,p,p1,p2,yp,yi,yw;
  int vmin[] = new int[max(w,h)];
  int vmax[] = new int[max(w,h)];
  int[] pix=img.pixels;
  int dv[]=new int[256*div];
  for (i=0;i<256*div;i++){
    dv[i]=(i/div);
  }

  yw=yi=0;

  for (y=0;y<h;y++){
    rsum=gsum=bsum=0;
    for(i=-radius;i<=radius;i++){
      p=pix[yi+min(wm,max(i,0))];
      rsum+=(p & 0xff0000)>>16;
      gsum+=(p & 0x00ff00)>>8;
      bsum+= p & 0x0000ff;
    }
    for (x=0;x<w;x++){

      r[yi]=dv[rsum];
      g[yi]=dv[gsum];
      b[yi]=dv[bsum];

      if(y==0){
        vmin[x]=min(x+radius+1,wm);
        vmax[x]=max(x-radius,0);
      }
      p1=pix[yw+vmin[x]];
      p2=pix[yw+vmax[x]];

      rsum+=((p1 & 0xff0000)-(p2 & 0xff0000))>>16;
      gsum+=((p1 & 0x00ff00)-(p2 & 0x00ff00))>>8;
      bsum+= (p1 & 0x0000ff)-(p2 & 0x0000ff);
      yi++;
    }
    yw+=w;
  }

  for (x=0;x<w;x++){
    rsum=gsum=bsum=0;
    yp=-radius*w;
    for(i=-radius;i<=radius;i++){
      yi=max(0,yp)+x;
      rsum+=r[yi];
      gsum+=g[yi];
      bsum+=b[yi];
      yp+=w;
    }
    yi=x;
    for (y=0;y<h;y++){
      pix[yi]=0xff000000 | (dv[rsum]<<16) | (dv[gsum]<<8) | dv[bsum];
      if(x==0){
        vmin[y]=min(y+radius+1,hm)*w;
        vmax[y]=max(y-radius,0)*w;
      }
      p1=x+vmin[y];
      p2=x+vmax[y];

      rsum+=r[p1]-r[p2];
      gsum+=g[p1]-g[p2];
      bsum+=b[p1]-b[p2];

      yi+=w;
    }
  }
}
