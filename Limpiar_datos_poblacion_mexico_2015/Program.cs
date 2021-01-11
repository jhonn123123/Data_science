using System.IO;
using System.Collections.Generic;
using System;
using System.Linq;


namespace mex
{
    class Program
    {
        static void Main(string[] args)
        {
            //Console.WriteLine("Hello World!");
            leer2();
            ordenarA();
            ordenarE();
            ordenarP();
        }

        public static void leer2()
        {
           
            var reader = new StreamReader(File.OpenRead(@"./mex.csv"));
            

            List<string> Estado = new List<string>();
            List<string> Extension= new List<string>();
            List<string> Poblacion= new List<string>();

            string[] row=new string[32];

            

            string[] State=new string[32];
            int[] Stencion=new int[32];
            int[] poblation=new int[32];

            string estado,extension,poblacion;
            while (!reader.EndOfStream)
            {
                var line = reader.ReadLine();
                var values = line.Split(',');

                estado=values[0].Replace("�",String.Empty);                
                extension=values[1].Replace("�",String.Empty);
                poblacion=values[2].Replace("�",String.Empty);
                

                estado=estado.Trim();
                extension=extension.Trim();
                poblacion=poblacion.Trim();

                Estado.Add(estado);
                Extension.Add(extension);
                Poblacion.Add( poblacion);

                
            }
                
                using (var w=File.CreateText(@"./newmex.csv"))
                {
                    for(int i=1;i<=32;i++)
                    {
                        var first=Estado[i];
                        var secon=Extension[i];
                        var tree=Poblacion[i];
                        var Line = string.Format("{0},{1},{2}",first,secon,tree);
                        w.WriteLine(Line);
                        
                    }
                }

                for(int i=1,j=0;i<33;i++,j++)
                {
                    //Console.WriteLine(Estado[i]+", "+Extension[i]+", "+Poblacion[i]);
                   

                    State[j]=Estado[i];
                    Stencion[j]=Int32.Parse(Extension[i]);
                    poblation[j]=Int32.Parse(Poblacion[i]);
                   
                    //Console.WriteLine(Estado2[i]+" "+Extension2[i]+" "+Poblacion2[i]);
                }

                promedio(State, Stencion,poblation);
        }

        public static void ordenarP()
        {
            string[] lines=System.IO.File.ReadAllLines(@"./newmex.csv");
            
            IEnumerable<string> query =  
            from line in lines  
            let x = line.Split(',')  
            orderby x[2] descending
            select x[0] + ", " + x[1] + ", " + x[2];  

            System.IO.File.WriteAllLines(@"./ordenadoPoblacionmex.csv", query.ToArray());  
            var reader = new StreamReader(File.OpenRead(@"./ordenadoPoblacionmex.csv"));
            Console.WriteLine("Ordenado por Poblacion: \n");
            while (!reader.EndOfStream)
            {
                var line = reader.ReadLine();
                Console.WriteLine(line);
            }
            Console.WriteLine();
              
        }

        public static void ordenarE()
        {
            string[] lines=System.IO.File.ReadAllLines(@"./newmex.csv");
            
            IEnumerable<string> query =  
            from line in lines  
            let x = line.Split(',')  
            orderby x[1] descending
            select x[0] + ", " + x[1] + ", " + x[2];  

            System.IO.File.WriteAllLines(@"./ordenadoExtensionmex.csv", query.ToArray()); 
            var reader = new StreamReader(File.OpenRead(@"./ordenadoExtensionmex.csv"));
            Console.WriteLine("Ordenado por Extension: \n");
            while (!reader.EndOfStream)
            {
                var line = reader.ReadLine();
                Console.WriteLine(line);
            } 
            Console.WriteLine();
        }
        
        public static void ordenarA()
        {
            string[] lines=System.IO.File.ReadAllLines(@"./newmex.csv");
            
            IEnumerable<string> query =  
            from line in lines  
            let x = line.Split(',')  
            orderby x[0] 
            select x[0] + ", " + x[1] + ", " + x[2];  

            System.IO.File.WriteAllLines(@"./ordenadoAlfabeticamentemex.csv", query.ToArray());
            
            var reader = new StreamReader(File.OpenRead(@"./ordenadoAlfabeticamentemex.csv"));
            Console.WriteLine("Ordenado Alfabeticamente: \n");
            while (!reader.EndOfStream)
            {
                var line = reader.ReadLine();
                Console.WriteLine(line);
            }
            Console.WriteLine();
        }

        public static void promedio(string[] Estados,int[] Extenciones,int[] Poblaciones)
        {
            double PE=0,PP=0;
            int suma=0,suma2=0;
            for(int i=0;i<32;i++)
            {
                suma=suma+Extenciones[i];
                suma2=suma2+Poblaciones[i];
                //Console.WriteLine(Extenciones[i]);
            }
            PE=(double)suma/32;
            PP=(double)suma2/32;

            
            Console.WriteLine("Total Extencion: "+suma);
            Console.WriteLine("Total Poblacion: "+suma2);
            Console.WriteLine("Promedio Extencion: "+PE);
            Console.WriteLine("Promedio Poblacion: "+PP);
            Console.WriteLine();
        }

        
    }
}
