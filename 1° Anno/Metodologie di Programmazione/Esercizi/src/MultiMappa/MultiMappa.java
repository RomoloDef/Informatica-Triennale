package MultiMappa;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.function.BiFunction;
import java.util.function.Predicate;


public class MultiMappa<K,V> {
	
	private Map<K,Set<V>> mappa;
	
	public MultiMappa() {
		mappa = new HashMap<K,Set<V>>();
		
	}
	
	// Metodo put - associa il valore alla chiave associata
	public void put(K k, V v) {
		// creo un insieme di appoggio per 
		// aggiungere il nuovo valore v che sto dando in input e poi aggiungerlo alla multimappa
		Set<V> insieme;
		// se la chiave esiste il mio insieme d'appoggio sarà mappa.get chiave
		// se la chiave non esiste l'insieme d'appoggio sarà un nuovo insieme
		if(mappa.containsKey(k)) {
			insieme = mappa.get(k);
		} else {
			insieme = new HashSet<V> ();
		}
		// ora che l'insieme è qualcosa di "concreto"
		insieme.add(v);
		mappa.put(k, insieme);
	}
	
	public Set<K> keySet() {
		return mappa.keySet();
	}
	
	public Set<V> get(K k) {
		return mappa.get(k);
	}
	
	// Metodo putAll - che aggiunge tutti gli elementi della multimappa in input alla mappa corrente.
	public void putAll(MultiMappa<K, V> mappa) {
		// itero sulle chiavi della multimappa in input
		for(K k:mappa.keySet()) {
			// inserisco nella multimappa "campo" le chiavi della multimappa in input e associo a queste chiavi il valore 
			// della multimappa in input
			this.mappa.put(k, mappa.get(k));
		}
	}
	
	// metodo removeAll - che rimuove tutte le chiavi della multimappa in input dalla mappa corrente.
	public void removeAll(MultiMappa<K, V> mappa) {
		for(K k:mappa.keySet()) {
			this.mappa.remove(k);
		}
	}
	
	// metodo get(k, p) - come sopra ma restituisce solo i valori che soddisfano il predicato p.
	public Set<V> get(K k, Predicate<V> p) {
		// ci creiamo un set di appoggio di valori
		Set <V> insieme = mappa.get(k);
		
		// iteriamo su questo insieme e tenere solo i valori che soddisfano il predicato cioè quelli per cui p.text = true
		// facendolo con un semplice for each non si può fare sulle collection quindi bisogna utilizzare iterator
		
		Iterator <V> iter = insieme.iterator();
		while(iter.hasNext()) {
			V v = iter.next();
			if(!p.test(v)) {
				insieme.remove(v);
			}
		}
		
		return insieme;
		
	}
	
	// Metodo values - che restituisce l’elenco (con duplicati) dei valori contenuti nella multimappa.
	public List<V> values() {
		List<V> valori = new ArrayList<V>();
		for(K k:mappa.keySet()) 
			valori.addAll(mappa.get(k));
		return valori;
	}
	
	// Metodo valueSet() - che restituisce l’insieme dei valori contenuti nella multimappa.
	public Set<V> valueSet() {
		Set <V> insieme = new HashSet<V>();
		for(Set<V> sv:mappa.values())
			insieme.addAll(sv);
		return insieme;
	}
	
	// Metodo transfomToMultiMappa - che restituisce una multimappa in cui le coppie (k, v) sono trasformate in (k, z) secondo una funzione (k, v) -> z (z pu`o essere di tipo 17 diverso rispetto a quello di v)
	
	public static <K,V,Z> MultiMappa<K,Z> transformToMultimppa(MultiMappa<K,V> mappa, BiFunction<K,V,Z> bf){
		//per esempio trasforma un multimappa dove K = Integer, V = Integer
		//in una multimappa iun cui K = Integer, V = String
		MultiMappa<K,Z> outputMap = new MultiMappa<K,Z>();
		for(K k:mappa.keySet()) {
			for(V v:mappa.get(k)) {
				Z z = bf.apply(k, v);
				outputMap.put(k, z);
			}
		}
		return outputMap;
	}
	
	public static void main(String[] args) {
		
	}
	

}
